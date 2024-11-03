from django.db import models


class ProductManager(models.Manager):

    def get_products_data(self):

        products = self.filter(is_active=True)
        product_data = []

        for product in products:
            sum_price = product.price * product.quantity

            product_info = {
                "id": product.id,
                "name": product.name,
                "image": product.image.url if product.image else None,
                "price": product.price,
                "quantity": product.quantity,
                "sum_price": sum_price,
                "category": [category.name for category in product.category.all()],
                "tags": [tag.name for tag in product.tag.all()],
                "slug": product.slug,
                "created_at": product.created_at,
                "updated_at": product.updated_at,
            }
            product_data.append(product_info)

        return product_data

    def get_product_by_id(self, product_id):
        try:
            product = self.get(id=product_id)
            return {
                "id": product.id,
                "name": product.name,
                "image": product.image.url if product.image else None,
                "price": product.price,
                "quantity": product.quantity,
                "category": [category.name for category in product.category.all()],
                "tags": [tag.name for tag in product.tag.all()],
                "slug": product.slug,
                "created_at": product.created_at,
                "updated_at": product.updated_at,
                "sum_price": product.price * product.quantity,
            }
        except:
            return None


class CategoryManager(models.Manager):

    def get_category_JSON(self):
        categories = self.all()
        data = []
        for category in categories:
            parent_name = category.parent.name if category.parent else None
            category_data = {
                "name": category.name,
                "parent": parent_name,
                "created_at": category.created_at,
                "updated_at": category.updated_at,
            }
            data.append(category_data)
        return data

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
