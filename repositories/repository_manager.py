from order.repositories.cart_repository import CartRepository
from order.repositories.order_item_repository import OrderItemRepository
from order.repositories.order_repository import OrderRepository
from product.repositories.category_repository import CategoryRepository
from product.repositories.product_repository import ProductRepository
from product.repositories.review_repository import ReviewRepository
from user.repositories.user_repository import UserRepository


class RepositoryManager:
    users = UserRepository
    categories = CategoryRepository
    products = ProductRepository
    orders = OrderRepository
    order_items = OrderItemRepository
    carts = CartRepository
    reviews = ReviewRepository
