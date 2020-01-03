from django.contrib import admin
from .models import FirstSatage, SecondStage, ThirdStage, ForthStage


@admin.register(FirstSatage)
class PostAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'course_author', 'book_name', 'book_isbn')
    list_filter = ('subject_name', 'course_author', 'book_name')
    search_fields = ('subject_name', 'course_author')
    ordering = ('course_author', 'subject_name')


@admin.register(SecondStage)
class PostAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'course_author', 'book_name', 'book_isbn')
    list_filter = ('subject_name', 'course_author', 'book_name')
    search_fields = ('subject_name', 'course_author')
    ordering = ('course_author', 'subject_name')


@admin.register(ThirdStage)
class PostAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'course_author', 'book_name', 'book_isbn')
    list_filter = ('subject_name', 'course_author', 'book_name')
    search_fields = ('subject_name', 'course_author')
    ordering = ('course_author', 'subject_name')

@admin.register(ForthStage)
class PostAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'course_author', 'book_name', 'book_isbn')
    list_filter = ('subject_name', 'course_author', 'book_name')
    search_fields = ('subject_name', 'course_author')
    ordering = ('course_author', 'subject_name')
