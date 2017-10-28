from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from site_user import views

urlpatterns = [
    url(r'^$', views.SiteUserView.as_view(), name='siteuser'),
    url(r'contact/$', views.ContactView.as_view(), name='contact-create'),
    url(r'skill/$', views.SkillListView.as_view(), name='skill-list'),
    url(r'experience/$', views.ExperienceListView.as_view(), name='experience-list'),
    url(r'education/$', views.EducationListView.as_view(), name='education-list'),
    url(r'project/$', views.ProjectListView.as_view(), name='project-list')
]

urlpatterns = format_suffix_patterns(urlpatterns)
