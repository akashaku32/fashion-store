from django.core.management.base import BaseCommand
from store.models import Product, Cart, CartItem, Customer
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Test cart functionality'

    def handle(self, *args, **options):
        # Create a test user if it doesn't exist
        user, created = User.objects.get_or_create(
            username='testuser',
            defaults={'email': 'test@example.com'}
        )
        if created:
            user.set_password('testpass123')
            user.save()
            self.stdout.write('Created test user')
        
        # Get or create customer
        customer, created = Customer.objects.get_or_create(user=user)
        if created:
            self.stdout.write('Created customer profile')
        
        # Get or create cart
        cart, created = Cart.objects.get_or_create(customer=customer)
        if created:
            self.stdout.write('Created cart')
        
        # Get first product
        product = Product.objects.first()
        if not product:
            self.stdout.write('No products found!')
            return
        
        self.stdout.write(f'Testing with product: {product.name}')
        
        # Clear existing cart items
        CartItem.objects.filter(cart=cart).delete()
        self.stdout.write('Cleared existing cart items')
        
        # Add product to cart
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, 
            product=product, 
            defaults={'quantity': 1}
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        
        self.stdout.write(f'Added to cart: {cart_item.quantity} x {cart_item.product.name}')
        
        # Check cart items
        cart_items = cart.cart_items.all()
        self.stdout.write(f'Cart items count: {len(cart_items)}')
        for item in cart_items:
            self.stdout.write(f'  - {item.quantity} x {item.product.name} = ₹{item.total_price}')
        
        # Test adding same product again
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, 
            product=product, 
            defaults={'quantity': 1}
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        
        self.stdout.write(f'Added again: {cart_item.quantity} x {cart_item.product.name}')
        
        # Check cart items again
        cart_items = cart.cart_items.all()
        self.stdout.write(f'Cart items count after second add: {len(cart_items)}')
        for item in cart_items:
            self.stdout.write(f'  - {item.quantity} x {item.product.name} = ₹{item.total_price}')
        
        self.stdout.write('Test completed!')
