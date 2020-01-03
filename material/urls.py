from django.urls import path
from .views import material, mat_resource, mat_course

app_name = 'material'
urlpatterns = [
    path('', material, name='material'),
    path('resources', mat_resource, name='resource'),
    path('courses', mat_course, name='courses'),
]
