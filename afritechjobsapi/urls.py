from django.urls import path
# from . import views
from afritechjobsapi.views.blog import blog_list, blog_detail
from afritechjobsapi.views.event import event_list, event_detail
from afritechjobsapi.views.work_resources import work_resources_list, work_resources_detail
from afritechjobsapi.views.hiring_guide import hiring_guide_list, hiring_guide_detail
from afritechjobsapi.views.category import job_category, job_category_detail
from afritechjobsapi.views.job_skills import job_skills, job_skills_detail
from afritechjobsapi.views.job_locations import job_locations, job_locations_detail
from afritechjobsapi.views.job_type import job_type
from afritechjobsapi.views.job_level import job_level
from afritechjobsapi.views.post_a_job import PostAJobListView, PostAJobView
# -------------------external api url-------------------------------
from afritechjobsapi.views.external_job_listings import ExternalJobListView, SecondExternalJobListView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("blog/", blog_list, name="blog_list"),
    path("blog/<int:id>", blog_detail, name="blog_detail"),
    path("event/", event_list, name="event_list"),
    path("event/<int:id>", event_detail, name="event_detail"),
    path("work-resources/", work_resources_list, name="work_resources_list"),
    path("work-resources/<int:id>", work_resources_detail, name="work_resources_detail"),
    path("hiring-guide/", hiring_guide_list, name="hiring_guide_list"),
    path("hiring-guide/<int:id>", hiring_guide_detail, name="hiring_guide_detail"),


    path("jobs/category/", job_category, name="job_category"),
    path("jobs/category/<int:id>/", job_category_detail, name="job_category_detail"),
    path("jobs/skills/", job_skills, name="job_skills"),
    path("jobs/skills/<int:id>/", job_skills_detail, name="job_skills_detail"),
    path("jobs/locations/", job_locations, name="job_locations"),
    path("jobs/locations/<int:id>/", job_locations_detail, name="job_locations_detail"),
    path("jobs/type/", job_type, name="job_type"),
    path("jobs/level", job_level, name="job_level"),

    # path("jobs/create", views.PostAJobListView.as_view(), name="post_a_job"),
    # path("jobs/", views.view_jobs, name="view_jobs"),
    # path("jobs/<int:id>", views.view_jobs_detail, name="view_jobs_detail"),

    # path('jobs/create', views.PostAJobView.as_view(), name='post_a_job'),
    # path('jobs/', views.PostAJobListView.as_view(), name='jobs'),
    # path('jobs/<int:pk>/', views.PostAJobDetailView.as_view(), name='post_a_job_single'),

# ------------------------------my own-----------------------------------
    # path('post-a-job/', views.PostAJobView.as_view(), name='post_a_job'),
    # path('jobs/', views.PostAJobListView.as_view(), name='jobs'),
    # path('post-a-job/<int:pk>/', views.PostAJobDetailView.as_view(), name='post_a_job_single'),
    # path('post-a-job/', PostAJobView.as_view(), name='post_a_job'),

    
    path('jobs/', PostAJobListView.as_view(), name='jobs'),
        # path('jobs/', PostAJobListView.as_view(), name='jobs-list'),
    path('jobs/<int:pk>/', PostAJobView.as_view(), name='job-detail'),
    path('post-a-job/', PostAJobListView.as_view(), name='post_a_job_list'),
    path('post-a-job/<int:pk>/', PostAJobView.as_view(), name='post_a_job_single'),

# ----------------------------external job api-------------------------------
    path('external-job-listing/', ExternalJobListView.as_view(), name='get_a_job_external'),
    path('external-job-listing_other/', SecondExternalJobListView.as_view(), name='a_job_external'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)
