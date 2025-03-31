from product.models import Review

class ReviewRepository:
    @staticmethod
    def get_all():
        return Review.objects.all()

    @staticmethod
    def get_by_id(review_id):
        return Review.objects.filter(id=review_id).first()

    @staticmethod
    def create(user, product, rating, comment):
        review = Review(user=user, product=product, rating=rating, comment=comment)
        review.save()
        return review
