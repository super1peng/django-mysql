from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^ajax_dict/$',views.ajax_dict,name='ajax-dict'),
]