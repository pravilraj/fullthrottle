from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import *
from .models import *


class UserData(APIView):
	serializer_class = UserSerializer
	permission_classes = (AllowAny,)

	def get(self, request):
		User = get_user_model()
		queryset = User.objects.all()
		serializer = self.serializer_class(queryset, many=True).data
		if not serializer:
			return Response({"ok":"false"})
		context = {
		"ok": True,
		"members": serializer
		}
		return Response(context)


class LoginDatas(APIView):
	serializer_class = LoginDataSerializer
	permission_classes = (AllowAny,)

	def get(self, request):
		queryset = LoginData.objects.all()
		serializer = self.serializer_class(queryset, many=True).data
		if not serializer:
			return Response({"ok":"false"})
		return Response(serializer)

	def post(self, request):
		serializer = LoginDataPOSTSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response("Upload successful", status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
