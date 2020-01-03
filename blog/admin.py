from django.contrib import admin
from .models import Post


#this code is to desing admin page 
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ''' we can include information about how to display the
        model in the admin site and how to interact with it.
    '''
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')