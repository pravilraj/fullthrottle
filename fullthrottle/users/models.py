from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager
import pytz, uuid, datetime


'''
Manipulate existing User table by appending extra REQUIRED_FIELDS'''

class CustomUser(AbstractUser):
	# getting all timezones
	TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
	# creating fields
	real_name = models.CharField(blank=True, max_length=100, unique=True)
	tz = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
	# generating random 10 digit id
	id = models.CharField(primary_key=True, default=uuid.uuid4().hex[:10], editable=False, max_length=10)
	username = None
	# use real name as username
	USERNAME_FIELD = 'real_name'
	REQUIRED_FIELDS = ['email']
	# mapping custom manager to user
	objects = CustomUserManager()


	def __str__(self):
		return self.real_name


'''
Creating login data table
'''
class LoginData(models.Model):
	user = models.ForeignKey(CustomUser, related_name = 'activity_periods', on_delete=models.CASCADE)
	start_time = models.DateTimeField(default=datetime.datetime.now)
	end_time = models.DateTimeField(default=datetime.datetime.now)