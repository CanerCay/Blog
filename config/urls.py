from django.conf.urls import  include, url
from rest_framework.urlpatterns import format_suffix_patterns
from config import views

urlpatterns =  [
    url(r'^$', views.SiteConfigView.as_view(), name='siteconfig-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)