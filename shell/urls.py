"""shell URL Configuration

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
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import django

from appointment import views
from . import settings

mtypes = '|'.join(settings.BOOKING_TYPES.keys())

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^(' + mtypes + r')/?$', views.view_booking_type),
    url(r'^(' + mtypes + r')/?$', views.view_booking_type),
    url(r'^(' + mtypes + r')/([1-2][0-9]{3})-([0-1][0-9])-([0-3][0-9])/?$', views.view_week),
    url(r'^book/(' + mtypes + r')/([1-2][0-9]{3})-([0-1][0-9])-([0-3][0-9])/([0-2][0-9])-([0-5][0-9])?$', views.booking_form)
] + staticfiles_urlpatterns()

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
