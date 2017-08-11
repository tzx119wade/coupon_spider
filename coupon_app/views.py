from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Coupon
# Create your views here.
@ensure_csrf_cookie
def index(request):
	return render(request,'index.html')
	
@ensure_csrf_cookie
def info(request):
	return render(request, 'info.html')

def search(request):
	return render(request, 'search.html')