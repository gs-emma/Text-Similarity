from django.urls import path 

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from similarity_site import settings

from . import views 

urlpatterns = [
    path('', views.get_submission),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()