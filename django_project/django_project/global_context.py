
from order.models import UserCart


def cart_items(request):
    total_items = 0
    if request.user.is_authenticated:
        cart = UserCart.objects.filter(user=request.user).first()
        if cart:
            total_items = sum(item.quantity for item in cart.items.all())
    return {
        'total_items': total_items,
    }