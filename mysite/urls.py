"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

# for media Folder
from django.conf import settings
from django.conf.urls.static import static

from .views import home_page, about_page, stage_page, exam_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='homePage'),
    path('about-us/', about_page, name='aboutPage'),
    path('stages/', stage_page, name='stagePage'),
    path('exam/', exam_page, name='testExam'),
    path('blog/', include('blog.urls',namespace='blog')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('material/', include('material.urls', namespace='material')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
