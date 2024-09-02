from django.contrib import admin

# Register your models here.
from .models import Blog, Event, WorkResources, HiringGuide, Category, PostAJob, JobLevel, JobLocations, JobSkills, JobType


# admin.site.register(Profile)
admin.site.register(Blog)
admin.site.register(Event)
admin.site.register(WorkResources)
admin.site.register(HiringGuide)
admin.site.register(Category)
admin.site.register(PostAJob)
admin.site.register(JobLevel)
admin.site.register(JobLocations)
admin.site.register(JobSkills)
admin.site.register(JobType)
