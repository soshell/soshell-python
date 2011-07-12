from django.template import Context, loader
from submissions.models import Submission
from django.http import HttpResponse

def index(request):
	subs = Submission.objects.all()
	t = loader.get_template('submissions/index.html')
	c = Context({
		'list': subs,
	})
	return HttpResponse(t.render(c))
