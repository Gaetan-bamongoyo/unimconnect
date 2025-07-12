from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomerUser(AbstractUser):
    photo = models.ImageField(upload_to='users', null=True)
    description = models.TextField(null=True)
    acces = models.IntegerField()

class Post(models.Model):
    description = models.TextField()
    lieu = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='posts')
    date_add = models.DateField(auto_now=True)
    user_id = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
