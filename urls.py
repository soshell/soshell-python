from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'soshell.views.home', name='home'),
    # url(r'^soshell/', include('soshell.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^submissions/$', 'submissions.views.index'),
    url(r'^submissions/(?P<sub_id>\d+)/$', 'submissions.views.detail'),
    url(r'^account/login/$',  login),
    url(r'^account/logout/$', logout),
)

urlpatterns += patterns('submissions.views',
    url(r'^submissions/$', 'index'),
    url(r'^$', 'index'),
    url(r'^submissions/(?P<sub_id>\d+)/$', 'detail'),
    url(r'^submissions/create/$', 'create'),
    url(r'^submissions/post_comment/$', 'post_comment'),
)
