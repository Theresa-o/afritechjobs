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
    
class HiringGuide(models.Model):
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
    
class JobSkills(models.Model):
    #more things to be added
    #skills options should change based on the selected category
    #https://stackoverflow.com/questions/3582544/django-model-choice-option-as-a-multi-select-box and https://stackoverflow.com/questions/15393134/django-how-can-i-create-a-multiple-select-form
    SKILLS_CHOICES = (
        ('Django', 'Django'),
        ('React', 'React'),
    )
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, choices=SKILLS_CHOICES)
    category = models.ManyToManyField(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class JobLocation(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class PostAJob(models.Model):
    job_title = models.CharField(max_length=200)
    job_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    job_skills = models.ManyToManyField
    job_salary_range = models.IntegerField(blank=True)
    job_type = models.ForeignKey(JobSkills, on_delete=models.SET_NULL)
    job_description = models.TextField()
    # job_type = 
    job_location = models.ForeignKey(JobLocation, on_delete=models.SET_NULL)
    # job_level
    # job_application_link
    # company_name
    # company_hq
    # company_logo
    # companys_website
    # company_contact_email
    # company_description

    








