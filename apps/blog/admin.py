from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'publish', 'status')
	list_filter = ('status', 'created', 'publish')
    # list_editable = ['status']
	search_fields = ('title', 'content')
	prepopulated_fields = {'slug': ('title',)}
	# raw_id_fields = ('author',)
	date_hierarchy = 'publish'
	ordering = ('status', 'publish')
