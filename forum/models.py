from django.db import models
from accounts.models import User

# Create your models here.


class Thread(models.Model):
    subject = models.CharField(max_length=50)
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
       ordering = ['-date']

    def __str__(self):
        return self.subject


class Comment(models.Model):
    content = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)






