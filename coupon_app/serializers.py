from .models import Coupon
from rest_framework_mongoengine import serializers

class CouponSerializers(serializers.DocumentSerializer):
	class Meta:
		model = Coupon
		fields = "__all__"