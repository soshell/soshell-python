from django.shortcuts import render_to_response
from submissions.models import Submission

def index(request):
	subs = Submission.objects.all()
	return render_to_response('submissions/index.html', {'list': subs})

def detail(request, sub_id):
	try:
		sub = Submission.objects.get(pk=sub_id)
	except Submission.DoesNotExist:
		raise Http404
	return render_to_response('submissions/details.html', {'submission': sub})

def post_comment(request):
	pass

