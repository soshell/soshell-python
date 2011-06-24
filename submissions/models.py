from django.db import models

# Create your models here.
class Submission(models.Model):
    title = models.CharField(max_length=200)
    submit_date = models.DateTimeField('date published')
    cache_views = models.IntegerField()
    def __unicode__(self):
       return self.title

class Tag(models.Model):
    submission = models.ForeignKey(Submission)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name
