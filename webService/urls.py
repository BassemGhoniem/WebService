"""webService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
<<<<<<< HEAD
from django.conf.urls import url

=======
from django.conf.urls import url, include
>>>>>>> f8e700d48baa872aa60dd2e554d24208cc62fc5c
from django.contrib import admin

from django.conf.urls import patterns, include, url


urlpatterns = [
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
    url(r'^blog/',include(blog.urls)),
=======
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
>>>>>>> f8e700d48baa872aa60dd2e554d24208cc62fc5c
]
