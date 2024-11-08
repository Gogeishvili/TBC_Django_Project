from django.core.management.base import BaseCommand
from order.models import CartItem,Product
from django.db.models import Count,Sum

class Command(BaseCommand):
    help = 'Popular products in cart'

    def handle(self, *args, **options):
        popular_products = (
            CartItem.objects
            .values('product')
            .annotate(
                user_count=Count('cart__user', distinct=True),
                total_quantity=Sum('quantity')
            )
            .order_by('-quantity')[:3] 
        )

        if popular_products:
            self.stdout.write('3 popular porduct')
            for item in popular_products:
                product = Product.objects.get(id=item['product'])
                self.stdout.write(
                    f'Product: {product.name}, '
                    f'Count in cart: {item["total_quantity"]}, '
                    f'user count: {item["user_count"]}'
                )
        else:
            self.stdout.write('Pdoruct not found')