from django.db import models
from solo.models import SingletonModel


class SiteConfiguration(SingletonModel):
    site_name = models.CharField(max_length=255, default='Site Name')
    site_description = models.CharField(max_length=500, default='Site Description')
    site_url = models.CharField(max_length=300, default='example.com')
    facebook = models.URLField(max_length=300, default='facebook.com')
    twitter = models.URLField(max_length=300, default='twitter.com')
    youtube = models.URLField(max_length=300, default='youtube.com')
    linkedin = models.URLField(max_length=300)
    github = models.URLField(max_length=300)
    maintenance_mode = models.BooleanField(default=False)
    contact_title = models.CharField(max_length=1000, default="Bu bölümden bana ulaşabilirsiniz.")

    def __str__(self):
        return u"Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"
