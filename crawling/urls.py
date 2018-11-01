from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.crawling_list, name="crawling_list"),
]