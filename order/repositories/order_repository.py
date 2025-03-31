from order.models import Order

class OrderRepository:
    @staticmethod
    def get_all():
        return Order.objects.all()

    @staticmethod
    def get_by_id(order_id):
        return Order.objects.filter(id=order_id).first()

    @staticmethod
    def create(user, total_price, status="pending"):
        order = Order(user=user, total_price=total_price, status=status)
        order.save()
        return order
