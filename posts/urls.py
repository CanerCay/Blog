from django.conf.urls import  include, url
from rest_framework.urlpatterns import format_suffix_patterns
from posts import views

urlpatterns =  [
    url(r'^$', views.PostList.as_view(), name='post-list'),
    url(r'^(?P<slug>[-\w]+)/$', views.PostDetail.as_view(), name='post-detail'),
]


urlpatterns = format_suffix_patterns(urlpatterns)