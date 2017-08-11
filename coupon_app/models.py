from mongoengine import *
from mongoengine import connect
connect('coupon_db', host='127.0.0.1', port=27017)

# Create your models here.
class Coupon(Document):
	img = StringField()
	created_date = StringField()
	coupon_price = StringField()
	name = StringField()
	coupon_url = StringField()
	cut_price = FloatField()
	activityId = StringField()
	num_receive = IntField()

	meta = {
		'ordering':['-created_date']
	}
