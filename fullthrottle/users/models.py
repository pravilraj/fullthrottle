from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager
import pytz, uuid, datetime

class CustomUser(AbstractUser):
	TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

	username = None
	email = models.EmailField(_('email address'), unique=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	real_name = models.CharField(blank=True, max_length=100)
	tz = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
	id = models.CharField(primary_key=True, default=uuid.uuid4().hex[:10], editable=False, max_length=10)

	def __str__(self):
		return self.real_name


class LoginData(models.Model):
	user = models.ForeignKey(CustomUser, related_name = 'activity_periods', on_delete=models.CASCADE)
	start_time = models.DateTimeField(default=datetime.datetime.now)
	end_time = models.DateTimeField(default=datetime.datetime.now)