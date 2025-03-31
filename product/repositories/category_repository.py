from product.models import Category

class CategoryRepository:
    @staticmethod
    def get_all():
        return Category.objects.all()

    @staticmethod
    def get_by_id(category_id):
        return Category.objects.filter(id=category_id).first()

    @staticmethod
    def create(name, slug):
        category = Category(name=name, slug=slug)
        category.save()
        return category
