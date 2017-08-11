# rest_framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests
# django core
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.decorators.csrf import csrf_protect
# self inside
from .serializers import CouponSerializers
from .models import Coupon

@api_view(['GET'])
@csrf_protect
def get_coupon(request, page):	
	query_set = Coupon.objects()
	page_robot = Paginator(query_set,12)

	try:
		page_data = page_robot.page(page)
	except PageNotAnInteger:
		page_data = page_robot.page(1)
	except EmptyPage:
		page_data = page_robot.page(page_robot.num_pages)

	serializer = CouponSerializers(page_data, many=True)

	body = {
		'total_page_num':page_robot.num_pages,
		'data': serializer.data,
	}

	return Response(body, status=status.HTTP_200_OK)

@api_view(['GET'])
@csrf_protect
def search(request, search_name, page_num):
	
	query_set = Coupon.objects(name__icontains=search_name)
	query_set_count = query_set.count()

	if query_set_count == 0:
		body = {
			'msg':'Nothing found',
			'code':1,
		}
		return Response(body, status=status.HTTP_404_NOT_FOUND)

	page_robot = Paginator(query_set,10)
	try:
		page_data = page_robot.page(page_num)
	except PageNotAnInteger:
		page_data = page_robot.page(1)
	except EmptyPage:
		body = {
			'msg':'Nothing left',
			'code':2,
		}
		return Response(body, status=status.HTTP_404_NOT_FOUND)

	total_page_num = page_robot.num_pages
	serializer = CouponSerializers(page_data, many=True)
	body = {
		'total_page_num':total_page_num,
		'data':serializer.data,
	}
	return Response(body, status=status.HTTP_200_OK)


@api_view(['GET'])
@csrf_protect
def search_coupon(request, search_keyword, page_num):

	api_url = 'http://m.huim.com/ajax/searchquan?key={}&p={}&s=1'.format(search_keyword, page_num)
	resp = requests.get(api_url)
	data = resp.json()['data']
	count = len(data)

	if count == 0:
		body = {
			'msg':'啥也没找到',
		}
		return Response(body, status=status.HTTP_404_NOT_FOUND)

	# 有数据的情况
	return Response(data, status=status.HTTP_200_OK)









