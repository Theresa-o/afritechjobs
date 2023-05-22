from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Category(models.Model):
    pass

class Profile(models.Model):
    pass

class Blog(models.Model):
    #reference - https://docs.djangoproject.com/en/2.1/ref/models/fields/#default and https://dbslusser.medium.com/setting-defaults-for-django-foreign-key-fields-c53cffb25a8c
    def deleted_author_replacement_default():
        return ("Incognito")

    title = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to="blog/%Y/%m/%d")
    content = models.TextField()
    category = models.ManyToManyField(Category, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    #This argument on the ForeignKey on_delete option requires you to set a default value when defining the relationship
    author = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, default=deleted_author_replacement_default, null=True)
    meta_description = models.CharField(max_length=150, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    post_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.author}"

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_details = models.TextField()
    banner_image = models.ImageField(upload_to="event")
    event_host = models.CharField(max_length=200)
    #not sure of the best way to handle this so that the creator would get a calendar and time popup to input the right date/time
    event_date = models.DateTimeField()
    registration_fees = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_attending = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.event_name} by {self.event_host}"
    
class WorkResources(models.Model):
    #reference - https://docs.djangoproject.com/en/2.1/ref/models/fields/#default and https://dbslusser.medium.com/setting-defaults-for-django-foreign-key-fields-c53cffb25a8c
    def deleted_author_replacement_default():
        return ("Incognito")

    title = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to="blog/%Y/%m/%d")
    content = models.TextField()
    category = models.ManyToManyField(Category, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    #This argument on the ForeignKey on_delete option requires you to set a default value when defining the relationship
    author = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, default=deleted_author_replacement_default, null=True)
    meta_description = models.CharField(max_length=150, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    post_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    is_email_confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()







