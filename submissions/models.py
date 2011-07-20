from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
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
	submit_date = models.DateTimeField('date created',auto_now_add=True)
	cache_views = models.IntegerField(default=0, blank=True)
	text = models.TextField(blank=True)
	image = models.ImageField(upload_to='images',blank=True)
	tags = models.ManyToManyField(Tag, blank=True)
	def __unicode__(self):
		return self.title

class SubmissionForm(ModelForm):
	tags = forms.CharField(widget=forms.MultipleHiddenInput,required=False)
	class Meta:
		model = Submission
		exclude = ('submit_date','cache_views',)

