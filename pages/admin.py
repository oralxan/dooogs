from django.contrib import admin

from .models import Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','description')
    list_display_links = ('id','title','description')
admin.site.register(Post,PostAdmin)
