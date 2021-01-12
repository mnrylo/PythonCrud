from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^$', views.index, name='index'),
    #####PROT####
    url(r'^cadprot$', views.cadprot, name='cadprot'),
    url(r'^create$', views.create, name='create'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^form/(?P<id>\d+)$', views.form, name='form'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^edit/form/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    #####RTA####
    url(r'^cadRTA$', views.cadRTA, name='cadRTA'),
    url(r'^createRTA$', views.createRTA, name='createRTA'),
    url(r'^editRTA/(?P<id>\d+)$', views.editRTA, name='editRTA'),
    url(r'^editRTA/updateRTA/(?P<id>\d+)$', views.updateRTA, name='updateRTA'),
    url(r'^deleteRTA/(?P<id>\d+)$', views.deleteRTA, name='deleteRTA'),
]