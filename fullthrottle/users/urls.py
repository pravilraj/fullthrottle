from django.conf.urls import url
from .views import *

urlpatterns = [
	# creating urls and mapping with apps
	url(r'^data/$', UserData.as_view(), name="user-data"),
	url(r'^logindata/$', LoginDatas.as_view(), name="login-data"),

	]
