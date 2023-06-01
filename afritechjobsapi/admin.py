from django.contrib import admin

# Register your models here.
from .models import Profile, Blog, Event, WorkResources, Category

admin.site.register(Profile)
admin.site.register(Blog)
admin.site.register(Event)
admin.site.register(WorkResources)
admin.site.register(Category)