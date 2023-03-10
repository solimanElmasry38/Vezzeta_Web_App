from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Search(models.Model):
    citys = [
        ("alex", "alex"),
        ("cairo", "cairo"),
    ]
    spec = [
        ("soolid", "soolid"),
        ("cardef", "cardef"),
        ("ssesf", "ssesf"),
        ("sefg", "sefg"),
        ("cardef", "cardef"),
    ]
    DocName = models.CharField(null=True, max_length=15, blank=True,)
    city = models.CharField(null=True, max_length=15,
                            blank=True, choices=citys)
    specialization = models.CharField(
        null=True, max_length=15, blank=True, choices=spec)

    def __str__(self):
        return self.DocName

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # img= models.ImageField(upload_to='uplaoad',blank=True)
    phone = models.IntegerField(blank=True, null=True, default=1)
    are_you_doctor = models.BooleanField(blank=True, null=True, default=True)

    def __str__(self):
        return str(self.user)

class Add(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True)
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(blank=True, null=True, max_length=50)
    price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    weatingHours = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    workingHours = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    img = models.ImageField(upload_to='uplaoad', blank=True)
    phone = models.IntegerField(blank=True, null=True, default=1)
    are_you_doctor = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def CreateProfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
