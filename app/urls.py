from app.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path("",home, name="home"),
    path("about/",about, name="abouts"),
    path("service/",service, name="service"),
    path("investment/",invest, name="invest"),
    path("grant/",grant, name="grant"),
    path("coverage/",coverage, name="coverage"),
    path("capital/",capital, name="capital"),
    path("contact/",contact, name="contact"),
    path("qoute/",qoute, name="qoute"),
    
]


if settings.DEBUG:  # Only serve media files during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)