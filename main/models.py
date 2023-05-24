from django.db import models

# Create your models here.
class UserInfo(models.Model):
    phonenumber = models.IntegerField(primary_key=True)
    name = models.TextField()
    gender = models.TextField()
    age = models.BinaryField
    accent = models.TextField()
    # voice = models.TextField()
    answer = models.TextField()
    mbti = models.CharField
    hobby = models.TextField()
    music = models.TextField()