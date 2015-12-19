"""djme_todos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
import os
from django.conf import settings

from django.conf.urls import include, url
from django.contrib import admin

from dddp.views import MeteorView

app = MeteorView.as_view(
    json_path=os.path.join(
        settings.SITE_ROOT, 'meteor', 'build', 'bundle', 'star.json'
    ),
)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {
            'document_root': settings.STATIC_ROOT,
            'show_indexes': False,
        },
    ),
    url(r'^(?P<path>.*)$', app),
]
