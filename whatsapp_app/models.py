from django.db import models
from django.db.models.signals import pre_save, post_save

from django.contrib.auth.models import  User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    phone_number = models.IntegerField(default='9408970364')
    
    def __str__(self):
        return self.user.username
    
    
def user_post_save_receiver_for_teacher(sender, instance, *args, **kwargs):
    try:
        user_profile = UserProfile.objects.get(user=instance)
    except:
       user_profile = None
    if user_profile is None:
        user_profile = UserProfile.objects.create(user=instance)
        user_profile.save()

post_save.connect(user_post_save_receiver_for_teacher, sender=User)