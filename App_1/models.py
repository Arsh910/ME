from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model) :
    name=models.CharField(max_length=20,blank=False,null=False)
    disc=models.CharField(max_length=50)
    img=models.ImageField(upload_to="images")
    author=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        max_length=100,
        default=1
    )
    def __str__(self):
        return self.name

