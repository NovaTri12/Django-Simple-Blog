from django.contrib import admin
from src.models import Post
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    list_display = ['id', 'title', 'short_content']
    summernote_fields = ['content']


admin.site.register(Post, PostAdmin)
