from django.shortcuts import render_to_response
from submissions.models import Submission, SubmissionForm
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def index(request):
	subs = Submission.objects.all()
	return render_to_response('submissions/index.html', {'list': subs})

def detail(request, sub_id):
	try:
		sub = Submission.objects.get(pk=sub_id)
	except Submission.DoesNotExist:
		raise Http404
	return render_to_response('submissions/details.html', {'submission': sub})

def create(request):
	if request.method == 'POST': # If the form has been submitted...
		form = SubmissionForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			submission = form.save()
			#subj = submission.subject
			return HttpResponseRedirect('/thanks/') # Redirect after POST
	else:
		form = SubmissionForm() # An unbound form
	return render_to_response('submissions/create.html',{'form': form}, context_instance=RequestContext(request))

@login_required
def account(request):
	pass

def post_comment(request):
	pass

def post_rating(request):
	pass
