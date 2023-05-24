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

class User(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name



