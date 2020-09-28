from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import *
from .models import *



'''
The class for creating Members using serializers 
'''
class UserData(APIView):
	serializer_class = UserSerializer

	# get members
	def get(self, request):
		# get user model
		User = get_user_model()
		# get all members
		queryset = User.objects.all()
		# pass the queryset to serializer
		serializer = self.serializer_class(queryset, many=True).data
		# check the serializer
		if not serializer:
			return Response({"ok": False})
		#creating object sructure
		context = {
		"ok": True,
		"members": serializer
		}
		return Response(context)
	# create members
	def post(self, request):
		# sent request data to serializer
		serializer = self.serializer_class(data=request.data)
		# check setializer
		if serializer.is_valid():
			serializer.save()
			return Response("Upload successful", status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginDatas(APIView):
	serializer_class = LoginDataSerializer

	# Post Login data
	def post(self, request):
		#pass request data to login data serializer
		serializer = LoginDataPOSTSerializer(data=request.data)
		# check seralizer
		if serializer.is_valid():
			serializer.save()
			return Response("Upload successful", status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
