from .models import Post
from django.contrib import admin
from mce_filebrowser.admin import MCEFilebrowserAdmin


class PostAdmin(MCEFilebrowserAdmin):
    pass


admin.site.register(Post, PostAdmin)
