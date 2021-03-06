#!/usr/bin/env python
# coding=utf-8

"""example URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from django.conf.urls import url, include
from django.contrib import admin

from django_otp.admin import OTPAdmin, AdminSite

from .views import IndexView


class TestAdminSite(admin.AdminSite):
    """test admin site."""

    login_form = AdminSite.login_form
    login_template = AdminSite.login_template

    def __init__(self, *args, **kwargs):
        """Init."""
        super(TestAdminSite, self).__init__(*args, **kwargs)
        self._registry = admin.site._registry.copy()


OTPAdmin.enable()
admin.site = AdminSite()

urlpatterns = [
    url(r'^s/', admin.site.urls),
    url(r'^qr/', include("django_otp.urls")),
    url(r'^index/', IndexView.as_view())
]
