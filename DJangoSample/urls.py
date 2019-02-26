from django.conf.urls import include, url
from django.contrib import admin
from DJangoSample.views import hello

urlpatterns = [
    # Examples:
    # url(r'^$', 'DJangoSample.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),

]
