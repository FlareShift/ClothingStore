from order.models import OrderItem

class OrderItemRepository:
    @staticmethod
    def get_all():
        return OrderItem.objects.all()

    @staticmethod
    def get_by_id(order_item_id):
        return OrderItem.objects.filter(id=order_item_id).first()

    @staticmethod
    def create(order, product, quantity, price):
        order_item = OrderItem(order=order, product=product, quantity=quantity, price=price)
        order_item.save()
        return order_item
