from user.models import User

class UserRepository:
    @staticmethod
    def get_all():
        return User.objects.all()

    @staticmethod
    def get_by_id(user_id):
        return User.objects.filter(id=user_id).first()

    @staticmethod
    def create(username, email, password, is_seller=False):
        user = User(username=username, email=email, is_seller=is_seller)
        user.set_password(password)
        user.save()
        return user
