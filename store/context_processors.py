from .models import Cart


def cart(request):
    """
    Add cart information to the template context
    """
    cart = None
    cart_items = []
    cart_total = 0
    cart_items_count = 0

    if request.user.is_authenticated:
        try:
            customer = request.user.customer
            cart, created = Cart.objects.get_or_create(customer=customer)
        except:
            pass
    else:
        if 'cart_id' in request.session:
            try:
                cart = Cart.objects.get(id=request.session['cart_id'])
            except Cart.DoesNotExist:
                del request.session['cart_id']

    if cart:
        cart_items = cart.items.all()
        cart_total = cart.total_price
        cart_items_count = cart.total_items

    return {
        'cart': cart,
        'cart_items': cart_items,
        'cart_total': cart_total,
        'cart_items_count': cart_items_count,
    }


