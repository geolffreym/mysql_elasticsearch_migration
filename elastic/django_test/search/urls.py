from django.conf.urls import patterns, url
from app.search.views import Search


urlpatterns = patterns('',
                       url(r'^get', Search.as_view(), name="search-view"),

)

