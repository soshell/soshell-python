from django.db import models

# Create your models here.
class Tag(models.Model):
	name = models.CharField(max_length=200)
	create_date = models.DateTimeField('date created')
	def __unicode__(self):
		return self.name

class Submission(models.Model):
	title = models.CharField(max_length=200)
	submit_date = models.DateTimeField('date published')
	cache_views = models.IntegerField()
	tags = models.ManyToManyField(Tag)
	def __unicode__(self):
		return self.title


