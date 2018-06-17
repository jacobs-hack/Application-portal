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
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from .views import registry as registry_views
from .views import setup as setup_views
from .views import edit as edit_views


urlpatterns = [
    # The Portal home page
    url(r'^$', registry_views.home, name='portal'),

    # Static requirements
    url(r'^imprint/$', TemplateView.as_view(template_name="static/imprint.html"), name='imprint'),
    url(r'^terms/$', TemplateView.as_view(template_name="static/terms.html"), name='terms'),

    # Login / Logout
    url(r'^login/$', auth_views.login, {'template_name': 'auth/login.html'},
        name='login'),
    url('^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    # Registration
    url('^register/$', setup_views.register, name='register'),

    # Initial data Setup
    # TODO: Update URLs
    url(r'^setup/$', setup_views.setup, name='setup'),
    url(r'^setup/academic/$', setup_views.academic, name='setup_academic'),
    url(r'^setup/application/$', setup_views.application, name='setup_application'),

    url(r'^setup/social/$', setup_views.social, name='setup_social'),
    url(r'^setup/skills/$', setup_views.skills, name='setup_skills'),

    # the portal for the user
    url(r'portal/', registry_views.portal, name='portal'),

    # Edit views
    # TODO: Update URLs
    url(r'^edit/$', edit_views.edit, name='edit'),
    url(r'^edit/password/$', edit_views.password, name='edit_password'),
    url(r'^edit/academic/$', edit_views.academic, name='edit_academic'),
    url(r'^edit/application/$', edit_views.application, name='edit_application'),

    url(r'^edit/social/$', edit_views.social, name='edit_social'),
    url(r'^edit/skills/$', edit_views.skills, name='edit_skills'),
]
