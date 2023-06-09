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
    path("jobs/create", views.post_a_job, name="post_a_job"),
    path("jobs/", views.view_jobs, name="view_jobs"),
    path("jobs/<int:id>", views.view_jobs_detail, name="view_jobs_detail"),
    
    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)


{
  "job_title": "Software Developer",
  "job_category": [
    {
      "id": 1,
      "name": "Engineering"
    },
    {
      "id": 2,
      "name": "IT"
    }
  ],
  "job_skills": [
    {
      "id": 1,
      "title": "DJ",
      "category": [
        {
          "id": 1,
          "name": "Web Development"
        },
        {
          "id": 2,
          "name": "Python"
        }
      ]
    },
    {
      "id": 2,
      "title": "RT",
      "category": [
        {
          "id": 3,
          "name": "Frontend Development"
        },
        {
          "id": 4,
          "name": "JavaScript"
        }
      ]
    }
  ],
  "job_salary_range": 80000,
  "job_description": "We are looking for a skilled software developer proficient in Django and React...",
  "job_type": {
    "id": 1,
    "job_type_choices": "FT"
  },
  "job_location": [
    {
      "id": 1,
      "name": "New York"
    },
    {
      "id": 2,
      "name": "San Francisco"
    }
  ],
  "job_level": [
    {
      "id": 1,
      "job_level_choices": "EL"
    },
    {
      "id": 2,
      "job_level_choices": "ML"
    }
  ],
  "job_application_link": "https://example.com/apply",
  "company_name": "ABC Company",
  "company_hq": "New York",
  "company_logo": "https://example.com/logo.png",
  "companys_website": "https://example.com",
  "company_contact_email": "info@example.com",
  "company_description": "ABC Company is a leading software development company...",
  "date_created": "2023-06-09T12:00:00Z",
  "date_updated": "2023-06-09T14:30:00Z"
}





{
  "job_title": "Software Developer",
  "job_category": [
    {
      "id": 1,
      "name": "Engineering"
    },
    {
      "id": 2,
      "name": "IT"
    }
  ],
  "job_skills": [
    {
      "id": 1,
      "title": "DJ",
      "category": [
        {
          "id": 1,
          "name": "Web Development"
        },
        {
          "id": 2,
          "name": "Python"
        }
      ]
    }
  ],
  "job_salary_range": 80000,
  "job_description": "We are looking for a skilled software developer proficient in Django...",
  "job_type": {
    "id": 1,
    "job_type_choices": "FT"
  },
  "job_location": [
    {
      "id": 1,
      "name": "New York"
    }
  ],
  "job_level": [
    {
      "id": 1,
      "job_level_choices": "EL"
    }
  ],
  "job_application_link": "https://example.com/apply",
  "company_name": "ABC Company",
  "company_hq": "New York",
  "company_logo": "https://example.com/logo.png",
  "companys_website": "https://example.com",
  "company_contact_email": "info@example.com",
  "company_description": "ABC Company is a leading software development company...",
  "date_created": "2023-06-09T12:00:00Z",
  "date_updated": "2023-06-09T14:30:00Z"
}
