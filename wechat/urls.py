"""wechat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('coupon_app.urls', namespace='coupon_app')),
]


# 定时任务
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from .coupon_spider import CouponSpider


def coupon_spider_job():
    spider = CouponSpider()
    spider.start_spider()
    print ('== 爬取完成 {}=='.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

scheduler = BackgroundScheduler()
scheduler.add_job(coupon_spider_job, 'interval', minutes=5)
scheduler.start()
