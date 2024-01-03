from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class profile(models.Model):
    user= models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    name=models.CharField(max_length=20,null=False,blank=False)
    bio=models.CharField(max_length=200,null=False,blank=False)
    image=models.ImageField(upload_to='user_photo')
    
    def __str__(self):
        return self.user.username

@receiver(post_save,sender=User)
def create_prof(sender,instance,created,**kwargs):
    if created:
        profile.objects.create(user=instance)