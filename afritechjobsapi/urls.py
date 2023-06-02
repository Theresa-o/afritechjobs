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
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)
