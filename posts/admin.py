# Django
from django.contrib import admin

#Models
from posts.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #Post admin#
    list_display = ('title', 'user', 'photo')
    list_display_links = ('user', 'photo', 'title')

    search_fields = (
        'user__username',
        'title'
    )
