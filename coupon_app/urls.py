from django.conf.urls import url
from . import views

from .api import get_coupon, search_coupon

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^info/$', views.info, name='info'),
	url(r'^search/', views.search, name='search'),

	# api
	url(r'^api/get_coupon/(?P<page>\d+)/$',get_coupon),
	url(r'^api/search/(?P<search_keyword>\w+)/(?P<page_num>\d+)/$',search_coupon),
]