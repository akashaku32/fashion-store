from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from .models import Category, Product, SeasonalGallery, Cart, CartItem

def home(request):
    # Get active categories
    categories = Category.objects.filter(is_active=True)
    
    # Get featured products
    featured_products = Product.objects.filter(
        is_featured=True,
        is_active=True
    )[:8]  # Limit to 8 featured products
    
    # Get current seasonal galleries
    current_date = timezone.now().date()
    seasonal_galleries = SeasonalGallery.objects.filter(
        is_active=True,
        start_date__lte=current_date,
        end_date__gte=current_date
    ).order_by('-start_date')[:4]  # Get latest 4 active galleries
    
    context = {
        'categories': categories,
        'featured_products': featured_products,
        'seasonal_galleries': seasonal_galleries,
    }
    
    return render(request, 'store/home.html', context)

def product_list(request):
    # Get all active products
    products = Product.objects.filter(is_active=True)
    
    # Filter by category if provided
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    # Filter by search query if provided
    search_query = request.GET.get('q')
    if search_query:
        products = products.filter(name__icontains=search_query)
    
    # Pagination
    paginator = Paginator(products, 12)  # Show 12 products per page
    page = request.GET.get('page')
    products = paginator.get_page(page)
    
    context = {
        'products': products,
        'categories': Category.objects.filter(is_active=True),
        'current_category': category_slug,
        'search_query': search_query,
    }
    
    return render(request, 'store/product_list.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    
    # Get related products from same category
    related_products = Product.objects.filter(
        category=product.category,
        is_active=True
    ).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    
    return render(request, 'store/product_detail.html', context)

@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    
    # Get or create cart
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(customer=request.user.customer)
    else:
        cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)
    
    # Add item to cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += quantity
        cart_item.save()
    
    return JsonResponse({
        'success': True,
        'cart_items_count': cart.total_items
    })

@require_POST
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Get cart
    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, customer=request.user.customer)
    else:
        cart = get_object_or_404(Cart, session_key=request.session.session_key)
    
    # Remove item from cart
    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.delete()
        success = True
    except CartItem.DoesNotExist:
        success = False
    
    return JsonResponse({
        'success': success,
        'cart_items_count': cart.total_items
    })

def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Add newsletter signup logic here
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})