from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^manage/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)
