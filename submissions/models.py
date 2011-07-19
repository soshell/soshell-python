from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from submissions.widgets import CommaTags
from django import forms

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField()

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

class SubmissionForm(ModelForm):
	tags = forms.ModelMultipleChoiceField(queryset=model.tag_set.all(), widget=CommaTags)
	class Meta:
		model = Submission

