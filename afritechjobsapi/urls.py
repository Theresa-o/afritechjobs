from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("blog/", views.blog_list, name="blog_list"),
    path("blog/<int:id>", views.blog_detail, name="blog_detail"),
    path("event/", views.event_list, name="event_list"),
    path("event/<int:id>", views.event_detail, name="event_detail"),
    path("work-resources/", views.work_resources_list, name="work_resources_list"),
    path("work-resources/<int:id>", views.work_resources_detail, name="work_resources_detail"),
    path("hiring-guide/", views.hiring_guide_list, name="hiring_guide_list"),
    path("hiring-guide/<int:id>", views.hiring_guide_detail, name="hiring_guide_detail"),
    path("jobs/category", views.job_category, name="job_category"),
    path("jobs/category/<int:id>", views.job_category_detail, name="job_category_detail"),
    path("jobs/skills", views.job_skills, name="job_skills"),
    path("jobs/skills/<int:id>", views.job_skills_detail, name="job_skills_detail"),
    path("jobs/locations", views.job_locations, name="job_locations"),
    path("jobs/locations/<int:id>", views.job_locations_detail, name="job_locations_detail"),
    path("jobs/type", views.job_type, name="job_type"),
    path("jobs/level", views.job_level, name="job_level"),

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

    path('post-a-job/', views.PostAJobView.as_view(), name='post_a_job'),
    path('jobs/', views.PostAJobListView.as_view(), name='jobs'),
    path('post-a-job/<int:pk>/', views.PostAJobView.as_view(), name='post_a_job_single'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)
