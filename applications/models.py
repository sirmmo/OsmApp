from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class App(models.Model):
	name = models.TextField()
	user = models.ForeignKey(User)
	apikey = models.TextField()

class AppFormat(models.Model):
	name = models.TextField()
	icon = models.TextField()

class Client(models.Model):
	app = models.ForeignKey(App)
	os = models.ForeignKey(AppFormat)
	client_key = models.TextField()
	namespace = models.TextField()
	default_code = models.BooleanField()


class ReadFilter(models.Model):
	name = models.TextField()
	app = models.ForeignKey(App)
	filters = models.TextField()

class WriteTemplate(models.Model):
	name = models.TextField()
	app = models.ForeignKey(App)
	template = models.TextField()


class WriteLog(models.Model):
	app = models.ForeignKey(App)
	client = models.ForeignKey(Client)
	user = models.ForeignKey(User)
	datetime = models.DateTimeField(auto_now=True)
	changeset = models.IntegerField()

class ReadLog(models.Model):
	app = models.ForeignKey(App)
	client = models.ForeignKey(Client)
	r_filter = models.ForeignKey(ReadFilter)


