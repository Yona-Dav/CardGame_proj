from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TypeProfile(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.ForeignKey(TypeProfile, to_field='name', default='beginner',on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='profile_pic/', default='https://t4.ftcdn.net/jpg/00/64/67/63/360_F_64676383_LdbmhiNM6Ypzb3FM4PPuFP9rHe7ri8Ju.jpg', blank=True, null=True)
    number_points = models.IntegerField(default=100)

    def pic(self):
        return self.image.url





