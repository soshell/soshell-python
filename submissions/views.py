from django.shortcuts import render_to_response
from submissions.models import Submission

def index(request):
	subs = Submission.objects.all()
	return render_to_response('submissions/index.html', {'list': subs})
