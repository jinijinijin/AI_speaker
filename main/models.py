from django.db import models

# Create your models here.
class UserInfo(models.Model):
    phonenumber = models.IntegerField(primary_key=True)
    name = models.TextField()
    gender = models.TextField()
    age = models.IntegerField(default=00)
    accent = models.TextField()
    # voice = models.TextField()
    answer = models.TextField()
    mbti = models.CharField(max_length=10, default='N/A')
    hobby = models.TextField()
    music = models.TextField()


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, name, password=None, **extra_fields):
        if not name:
            raise ValueError('The Name field must be set')

        # phone_number 값을 password로 사용
        extra_fields.setdefault('phone_number', password)

        user = self.model(name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        return self.create_user(name, password, **extra_fields)

class User(AbstractBaseUser):
    name = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)  # phone_number 필드로 사용
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []