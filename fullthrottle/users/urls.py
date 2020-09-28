from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^data/$', UserData.as_view(), name="user-data"),
	url(r'^ldata/$', LoginDatas.as_view(), name="login-data"),

	]
