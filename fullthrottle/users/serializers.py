from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *


class LoginDataSerializer(serializers.ModelSerializer):
	
	class Meta:

		model = LoginData
		fields = ['start_time','end_time',]


class UserSerializer(serializers.ModelSerializer):
	activity_periods = LoginDataSerializer(read_only = True, many=True)

	class Meta:
		model = get_user_model()
		fields = [
		'id',
		'real_name',
		'tz',
		'activity_periods',
		]


class LoginDataPOSTSerializer(serializers.ModelSerializer):
	
	class Meta:

		model = LoginData
		fields = ['start_time','end_time','user',]