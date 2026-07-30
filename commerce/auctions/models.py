from tabnanny import check
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class listing(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True,
                          serialize=False, verbose_name='ID')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_key")
    t = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    start_bid = models.IntegerField(null=False)
    current = models.IntegerField(null=False)
    img = models.URLField(max_length=300)
    ctg = models.CharField(max_length=100)
    fav = models.BooleanField(default=False)


class bids(models.Model):
    bid = models.IntegerField(null=False)
    listings = models.ForeignKey(listing, on_delete=models.CASCADE)
    userbid = models.ForeignKey(User, on_delete=models.CASCADE)


class comment(models.Model):
    chk = models.CharField(max_length=200)
    cmnt = models.CharField(max_length=500)
    usercmnt = models.ForeignKey(User, on_delete=models.CASCADE)
    listingcmnt = models.ForeignKey(listing, on_delete=models.CASCADE)


class selled(models.Model):
    t = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    img = models.URLField(max_length=300)
    salle_price = models.IntegerField(null=False)
    salles = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="salles")
    touser = models.ForeignKey(User, on_delete=models.CASCADE)
