from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'turnkey_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'views.index', {"template": "index.html"}, name="index"),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
)
