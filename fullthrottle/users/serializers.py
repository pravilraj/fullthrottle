from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *


class LoginDataSerializer(serializers.ModelSerializer):
	
	class Meta:
		# bind serializer with model
		model = LoginData
		# specify the fields from Login data model
		fields = ['start_time','end_time',]


class UserSerializer(serializers.ModelSerializer):
	# create nested serializer and append login data to activity_periods
	activity_periods = LoginDataSerializer(read_only = True, many=True)

	class Meta:
		# get user model
		model = get_user_model()
		# specify the fields from Login data model
		fields = ['id', 'real_name', 'tz', 'activity_periods',]


# Post serializer for login Data
class LoginDataPOSTSerializer(serializers.ModelSerializer):
	
	class Meta:

		model = LoginData
		fields = ['start_time','end_time','user',]