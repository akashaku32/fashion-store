from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q, Avg
from django.utils import timezone
from .models import (
    Product, Category, Cart, CartItem, Customer, Address, 
    Order, OrderItem, Review, Newsletter
)
from .forms import ReviewForm, NewsletterForm, CheckoutForm
import uuid


def home(request):
    """Home page with featured products and categories"""
    featured_products = Product.objects.filter(is_featured=True, is_active=True)[:8]
    categories = Category.objects.filter(is_active=True)[:6]
    latest_products = Product.objects.filter(is_active=True)[:8]
    
    context = {
        'featured_products': featured_products,
        'categories': categories,
        'latest_products': latest_products,
    }
    return render(request, 'store/home.html', context)


def product_list(request):
    """Product listing page with filtering and pagination"""
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.filter(is_active=True)
    
    # Filtering
    category_slug = request.GET.get('category')
    search_query = request.GET.get('search')
    sort_by = request.GET.get('sort', 'newest')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    size = request.GET.get('size')
    color = request.GET.get('color')
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    if size:
        products = products.filter(size=size)
    if color:
        products = products.filter(color=color)
    
    # Sorting
    if sort_by == 'price_low':
        products = products.order_by('price')
    elif sort_by == 'price_high':
        products = products.order_by('-price')
    elif sort_by == 'name':
        products = products.order_by('name')
    else:  # newest
        products = products.order_by('-created_at')
    
    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    
    context = {
        'products': products,
        'categories': categories,
        'current_category': category_slug,
        'search_query': search_query,
        'sort_by': sort_by,
        'min_price': min_price,
        'max_price': max_price,
        'size': size,
        'color': color,
    }
    return render(request, 'store/product_list.html', context)


def product_detail(request, slug):
    """Product detail page"""
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related_products = Product.objects.filter(
        category=product.category, 
        is_active=True
    ).exclude(id=product.id)[:4]
    
    reviews = Review.objects.filter(product=product, is_approved=True)
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    
    # Handle review submission
    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.customer = request.user.customer
            review.save()
            messages.success(request, 'Your review has been submitted and is pending approval.')
            return redirect('store:product_detail', slug=slug)
    else:
        form = ReviewForm()
    
    context = {
        'product': product,
        'related_products': related_products,
        'reviews': reviews,
        'average_rating': average_rating,
        'form': form,
    }
    return render(request, 'store/product_detail.html', context)


def add_to_cart(request, product_id):
    """Add product to cart"""
    product = get_object_or_404(Product, id=product_id, is_active=True)
    quantity = int(request.POST.get('quantity', 1))
    
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer=customer)
    else:
        if 'cart_id' in request.session:
            try:
                cart = Cart.objects.get(id=request.session['cart_id'])
            except Cart.DoesNotExist:
                cart = None
        else:
            cart = None
            
        if not cart:
            cart = Cart.objects.create(session_key=str(uuid.uuid4()))
            request.session['cart_id'] = cart.id
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': quantity}
    )
    
    if not created:
        cart_item.quantity += quantity
        cart_item.save()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'message': 'Product added to cart successfully',
            'cart_items_count': cart.total_items
        })
    
    messages.success(request, f'{product.name} added to cart successfully!')
    return redirect('store:cart')


def remove_from_cart(request, cart_item_id):
    """Remove item from cart"""
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'message': 'Item removed from cart'
        })
    
    messages.success(request, 'Item removed from cart')
    return redirect('store:cart')


def update_cart_item(request, cart_item_id):
    """Update cart item quantity"""
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity <= 0:
        cart_item.delete()
    else:
        cart_item.quantity = quantity
        cart_item.save()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'message': 'Cart updated successfully',
            'cart_total': cart_item.cart.total_price,
            'cart_items_count': cart_item.cart.total_items
        })
    
    return redirect('store:cart')


def cart_view(request):
    """Shopping cart page"""
    cart = None
    cart_items = []
    
    if request.user.is_authenticated:
        try:
            customer = request.user.customer
            cart = Cart.objects.get(customer=customer)
            cart_items = cart.items.all()
        except:
            pass
    else:
        if 'cart_id' in request.session:
            try:
                cart = Cart.objects.get(id=request.session['cart_id'])
                cart_items = cart.items.all()
            except Cart.DoesNotExist:
                del request.session['cart_id']
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
    }
    return render(request, 'store/cart.html', context)


@login_required
def checkout(request):
    """Checkout page"""
    customer = request.user.customer
    cart = Cart.objects.filter(customer=customer).first()
    
    if not cart or not cart.items.exists():
        messages.warning(request, 'Your cart is empty.')
        return redirect('store:cart')
    
    addresses = Address.objects.filter(customer=customer)
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Create order
            order = Order.objects.create(
                customer=customer,
                shipping_address=form.cleaned_data['shipping_address'],
                billing_address=form.cleaned_data['billing_address'],
                subtotal=cart.total_price,
                shipping_cost=10.00,  # Fixed shipping cost
                tax_amount=cart.total_price * 0.08,  # 8% tax
                total_amount=cart.total_price + 10.00 + (cart.total_price * 0.08),
                notes=form.cleaned_data['notes']
            )
            
            # Create order items
            for cart_item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.final_price,
                    total_price=cart_item.total_price
                )
            
            # Clear cart
            cart.items.all().delete()
            
            messages.success(request, f'Order {order.order_number} placed successfully!')
            return redirect('store:order_success', order_id=order.id)
    else:
        form = CheckoutForm()
        if addresses.exists():
            form.fields['shipping_address'].initial = addresses.filter(is_default=True).first()
            form.fields['billing_address'].initial = addresses.filter(is_default=True).first()
    
    context = {
        'form': form,
        'cart': cart,
        'addresses': addresses,
    }
    return render(request, 'store/checkout.html', context)


def order_success(request, order_id):
    """Order success page"""
    order = get_object_or_404(Order, id=order_id, customer=request.user.customer)
    return render(request, 'store/order_success.html', {'order': order})


@login_required
def order_history(request):
    """User's order history"""
    orders = Order.objects.filter(customer=request.user.customer).order_by('-created_at')
    return render(request, 'store/order_history.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    """Order detail page"""
    order = get_object_or_404(Order, id=order_id, customer=request.user.customer)
    return render(request, 'store/order_detail.html', {'order': order})


def newsletter_signup(request):
    """Newsletter signup"""
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Successfully subscribed to newsletter!'})
            messages.success(request, 'Successfully subscribed to newsletter!')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'Email already subscribed or invalid.'})
            messages.error(request, 'Email already subscribed or invalid.')
    
    return redirect('store:home')


def about(request):
    """About page"""
    return render(request, 'store/about.html')


def contact(request):
    """Contact page"""
    if request.method == 'POST':
        # Handle contact form submission
        messages.success(request, 'Thank you for your message. We will get back to you soon!')
        return redirect('store:contact')
    
    return render(request, 'store/contact.html')


