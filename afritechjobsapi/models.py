from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    is_email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return (self.user)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Blog(models.Model):
    def deleted_author_replacement_default():
        #TODO figure out how to change this to a string without returning errors
        return (1)

    title = models.CharField(max_length=255, unique=True)
    # image = models.ImageField(upload_to="blog/%Y/%m/%d")
    content = models.TextField()
    category = models.ManyToManyField(Category, null=True, blank=True)
    # slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, default=deleted_author_replacement_default, null=True)
    meta_description = models.CharField(max_length=150, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    post_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.author}"

class Event(models.Model):
    def deleted_author_replacement_default():
        return (1)
    
    event_name = models.CharField(max_length=200)
    author = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, default=deleted_author_replacement_default, null=True)
    event_details = models.TextField()
    # banner_image = models.ImageField(upload_to="event")
    event_host = models.CharField(max_length=200)
    event_date = models.DateTimeField()
    registration_fees = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_attending = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.event_name} by {self.event_host}"
    
class WorkResources(models.Model):
    def deleted_author_replacement_default():
        return (1)

    title = models.CharField(max_length=255, unique=True)
    # image = models.ImageField(upload_to="blog/%Y/%m/%d")
    content = models.TextField()
    category = models.ManyToManyField(Category, null=True, blank=True)
    # slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, default=deleted_author_replacement_default, null=True)
    meta_description = models.CharField(max_length=150, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    post_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.author}"
    








