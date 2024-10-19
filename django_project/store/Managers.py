from django.db import models


class ProductManager(models.Manager):

    def get_products_info_List(self):
        products = self.all()
        data = []

        for product in products:
            category_names = product.category.values_list("name")

            product_data = {
                "name": product.name,
                "categories": list(category_names),
                "image_url": product.image.url if product.image else None,
                "price": str(product.price),
                "quantity": product.quantity,
                "is_active": product.is_active,
                "created_at": product.created_at,
                "updated_at": product.updated_at,
            }

            data.append(product_data)

        return data

    def get_all_active_products(self):
        return self.filter(is_active=True)


class CategoryManager(models.Manager):
    
    def get_category_summary(self):
        categories = self.prefetch_related("products").all()

        category_data = []
        for category in categories:
            products_summary = []
            for product in category.products.all():
                total_price = product.price * product.quantity
                products_summary.append(
                    {"product_name": product.name, "total_price": total_price}
                )

            category_data.append(
                {"category_name": category.name, "products_summary": products_summary}
            )

        return category_data

    def get_most_expensive_product(self):
        categories = self.prefetch_related("products").all()

        category_data = []
        for category in categories:
            most_expensive_product = category.products.order_by("-price").first()

            category_data.append(
                {
                    "category_name": category.name,
                    "most_expensive": (
                        {
                            "name": most_expensive_product.name,
                            "price": most_expensive_product.price,
                        }
                        if most_expensive_product
                        else None
                    ),
                }
            )

        return category_data

    def get_cheapest_product(self):
        categories = self.prefetch_related("products").all()

        category_data = []
        for category in categories:
            cheapest_product = category.products.order_by("price").first()

            category_data.append(
                {
                    "category_name": category.name,
                    "cheapest": (
                        {
                            "name": cheapest_product.name,
                            "price": cheapest_product.price,
                        }
                        if cheapest_product
                        else None
                    ),
                }
            )

        return category_data

    def get_average_product_price(self):
        categories = self.prefetch_related("products").all()

        category_data = []
        for category in categories:
            average_price = 0
            if category.products.exists():
                total_price = sum(product.price for product in category.products.all())
                average_price = total_price / category.products.count()

            category_data.append(
                {
                    "category_name": category.name,
                    "average_price": round(average_price, 2),
                }
            )

        return category_data
