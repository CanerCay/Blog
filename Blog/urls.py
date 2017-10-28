from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()
from Blog.views import home

urlpatterns = [
                  url(r'^admin/', include(admin.site.urls)),
                  url(r'^api-auth/', include('rest_framework.urls',
                                             namespace='rest_framework')),
                  # index
                  url(r'^$', home, name="home"),
                  # config
                  url(r'^config/', include('config.urls')),
                  # user
                  url(r'^aboutme/', include('site_user.urls')),
                  # posts
                  url(r'^posts/', include('posts.urls')),
                  # tags
                  url(r'^tags/', include('tags.urls')),
                  # Kokoloji testi mobil uygulama api ve web veri giriş sayfası
                  url(r'^docs/', include('rest_framework_docs.urls')),
                  # Html Editor
                  url(r'^tinymce/', include('tinymce.urls')),
                  # Html Editor File Upload
                  url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
