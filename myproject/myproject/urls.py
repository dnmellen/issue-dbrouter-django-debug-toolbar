from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from myapp.views import Index

urlpatterns = patterns('',
    # Examples:
    url(r'^$', Index.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
