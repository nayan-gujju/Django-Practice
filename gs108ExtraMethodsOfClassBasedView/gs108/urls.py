"""gs108 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from school import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='myfun'),
    path('mycls/', views.MyHomeView.as_view(), name='myclass'),
    path('aboutfun/', views.aboutfun, name='aboutfun'),
    path('aboutcls/', views.MyAboutView.as_view(), name='aboutclass'),
    path('formfun/', views.contactfun, name='formfun'),
    path('formcls/', views.ContactForm.as_view(), name='formclass'),
    path('newsfun/', views.newsfun,{'template_name':'school/news.html'} ,name='newsfun'),
    path('newscls/', views.NewsClass.as_view(),{'template_name':'school/news.html'} ,name='newsclass'),
]
