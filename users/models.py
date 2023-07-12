from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        RECRUITER = "RECRUITER", 'Recruiter'
        CANDIDATE = "CANDIDATE", 'Candidate'

    #the default role is admin cause if a recruiter is to be signed up, there would be register page for that
    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)

    # USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)
        
    def __str__(self):
        return self.email
        
#this recruitermanager helps filter for only recruiters by tapping into .recruiter i.e Recruiter.recruiter.all() - we can filter for just recruiters
        
class RecruiterManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            return ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email).lower(),
            password = password,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.RECRUITER)

class Recruiter(User):
    base_role = User.Role.RECRUITER

    recruiter = RecruiterManager()

    class Meta:
        proxy = True

class RecruiterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

@receiver(post_save, sender=Recruiter)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "RECRUITER":
        RecruiterProfile.objects.create(user=instance)

# @receiver(post_save, sender=Recruiter)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created and instance.role == "RECRUITER":
#         RecruiterProfile.objects.update(user=instance)
#     instance.RecruiterProfile.save()


class CandidateManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            return ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email).lower(),
            password = password,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CANDIDATE)

class Candidate(User):
    base_role = User.Role.CANDIDATE

    candidate = CandidateManager()

    class Meta:
        proxy = True

class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

@receiver(post_save, sender=Candidate)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "CANDIDATE":
        CandidateProfile.objects.create(user=instance)


    

