from order.models import Cart

class CartRepository:
    @staticmethod
    def get_all():
        return Cart.objects.all()

    @staticmethod
    def get_by_id(cart_id):
        return Cart.objects.filter(id=cart_id).first()

    @staticmethod
    def create(user, product, quantity=1):
        cart = Cart(user=user, product=product, quantity=quantity)
        cart.save()
        return cart
