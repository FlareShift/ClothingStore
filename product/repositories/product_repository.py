from product.models import Product

class ProductRepository:
    @staticmethod
    def get_all():
        return Product.objects.all()

    @staticmethod
    def get_by_id(product_id):
        return Product.objects.filter(id=product_id).first()

    @staticmethod
    def create(name, description, price, stock, category, image):
        product = Product(name=name, description=description, price=price, stock=stock, category=category, image=image)
        product.save()
        return product
