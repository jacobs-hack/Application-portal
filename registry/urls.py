"""Registry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.shortcuts import redirect

from .views import registry as registry_views
from .views import setup as setup_views
from .views import edit as edit_views
from .views import cv as cv_views
from .views import auth as auth_views

# Side-effect import: Initialize hooks
import hacker.hooks


urlpatterns = [
    # The Portal home page
    path('', registry_views.home, name='portal'),

    # Static requirements
    path('imprint/', lambda request: redirect(settings.IMPRINT_URL), name='imprint'),
    path('terms/', lambda request: redirect(settings.TERMS_URL), name='terms'),
    path('privacy/', lambda request: redirect(settings.PRIVACY_URL), name='privacy'),

    # Login / Logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Registration
    #path('register/', setup_views.register, name='register'),
    path('register/', registry_views.register, name='register'),

    # Initial data Setup
    path('setup/', setup_views.setup, name='setup'),
    path('setup/academic/', setup_views.academic, name='setup_academic'),
    path('setup/application/', setup_views.application, name='setup_application'),
    path('setup/organizational/', setup_views.organizational, name='setup_organizational'),
    path('setup/cv/', setup_views.cv, name='setup_cv'),

    # the portal for the user
    path('portal/', registry_views.portal, name='portal'),

    # Edit views
    path('edit/', edit_views.edit, name='edit'),
    path('edit/password/', edit_views.password, name='edit_password'),
    path('edit/academic/', edit_views.academic, name='edit_academic'),
    path('edit/application/', edit_views.application, name='edit_application'),
    path('edit/organizational/', edit_views.organizational, name='edit_organizational'),
    path('edit/cv/', edit_views.cv, name='edit_cv'),
    path('edit/rsvp/', edit_views.rsvp, name='edit_rsvp'),

    # CV Media URL
    re_path('^{}cvs/(?P<username>[\w.@+-]+)\.pdf$'.format(settings.MEDIA_URL[1:]), cv_views.cv, name='view_cv')
]