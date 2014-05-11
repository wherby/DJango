from django.conf.urls import patterns, include, url
import os.path
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/(?P<path>.*)$','django.views.static.serve',
        {'document_root':os.path.normcase('C:/Python27\\Lib\\site-packages\\django\\bin\\cms\\tinymce\\js\\tinymce')}),
    url(r'^search', 'search.views.search'),
    url(r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$','coltrane.views.entry_detail'),
    url(r'^weblog/$', 'coltrane.views.entries_index'),
    url(r'',include('django.contrib.flatpages.urls')),
)
