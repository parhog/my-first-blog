from django.db import models
from django.utils import timezone

# Create your models here.

class post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	tect = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	
	def Publish(self):
		self.published_date = Timezone.now()
		self.save()
		
	def __str__(self):
		return self.title
		
