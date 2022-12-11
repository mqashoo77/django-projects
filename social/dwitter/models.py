from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False, # العلاقة مش عكسية
        blank=True # مش ضروري يكون عندك فلورز
    )
    def __str__(self):
        return self.user.username

# def create_profile(sender, instance, created, **kwargs): # حذفتها عشان استخدم الديكوريتر 
#     if created:
#         user_profile = Profile(user=instance)
#         user_profile.save()
#         user_profile.follows.set([instance.profile.id])
#         user_profile.save()

# Create a Profile for each new user.
# post_save.connect(create_profile, sender=User) 

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()



    