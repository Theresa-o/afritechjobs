from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True, blank=True)

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
    #TODOskills options should change based on the selected category

    title = models.CharField(max_length=20, unique=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

class JobLocations(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class JobType(models.Model):
    CONTRACT = 'CT'
    FULLTIME = 'FT'
    FREELANCE = 'FL'
    INTERNSHIP = 'IP'
    PARTTIME = 'PT'

    JOB_TYPE_CHOICES = [
        (CONTRACT, "Contract"),
        (FULLTIME, "FullTime"),
        (FREELANCE, "Freelance"),
        (INTERNSHIP, "Internship"),
        (PARTTIME, "Parttime"),
    ]

    job_type_choices = models.CharField(max_length=2, choices=JOB_TYPE_CHOICES, default=FULLTIME,)


class JobLevel(models.Model):

    STUDENT = 'ST'
    INTERN = 'IN'
    ENTRYLEVEL = 'EL'
    MIDLEVEL = 'ML'
    SENIORLEVEL = 'SL'
    COFOUNDER = 'CF'
    DIRECTOR = 'DC'
    MANAGER = 'MG'
    CEO = 'CEO'
    CTO = 'CTO'
    CMO = 'CMO'
    CFO = 'CFO'
    COO = 'COO'

    JOB_LEVEL_CHOICES = [
        (STUDENT, "Student"),
        (INTERN, "Intern"),
        (ENTRYLEVEL, "Entrylevel"),
        (MIDLEVEL, "Midlevel"),
        (SENIORLEVEL, "Seniorlevel"),
        (COFOUNDER, "Cofounder"),
        (DIRECTOR, "Director"),
        (MANAGER, "Manager"),
        (CEO, "Chief Executive Officer"),
        (CTO, "Chief Technology Officer"),
        (CMO, "Chief Marketing Officer"),
        (COFOUNDER, "Cofounder"),
        (CFO, "Chief Financial Officer"),
        (COO, "Chief Operating Officer"),
    ]
    
    job_level_choices = models.CharField(max_length=3, choices=JOB_LEVEL_CHOICES, default=ENTRYLEVEL)


class PostAJob(models.Model):
    job_title = models.CharField(max_length=200)
    job_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    job_skills = models.ManyToManyField(JobSkills, null=True, blank=True)
    job_salary_range = models.IntegerField(blank=True)
    job_description = models.TextField()
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)
    job_location = models.ForeignKey(JobLocations, on_delete=models.CASCADE, default='')
    job_level = models.ForeignKey(JobLevel, on_delete=models.CASCADE)
    job_application_link = models.URLField(max_length=200)
    company_name = models.CharField(max_length=200)
    company_hq = models.CharField(max_length=200)
    company_logo = models.ImageField()
    companys_website = models.URLField(max_length=200)
    company_contact_email = models.EmailField(max_length=200, null=True, blank=True)
    company_description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.job_title

    








