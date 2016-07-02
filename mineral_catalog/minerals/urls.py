from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^$', views.mineral_list, name='list'),
    url(r'(?P<pk>\d+)/$', views.mineral_detail, name='detail'),
    url(r'(?P<first_letter>[a-z])/$', views.mineral_startswith,
        name='startswith'),
]
urlpatterns += staticfiles_urlpatterns()