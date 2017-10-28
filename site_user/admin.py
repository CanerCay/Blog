from django.contrib import admin
from solo.admin import SingletonModelAdmin
from site_user.models import SiteUser, Skill, Experience, Education, Project, Contact

admin.site.register(SiteUser, SingletonModelAdmin)

admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Contact)
