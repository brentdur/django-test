from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse
from .models import Question
from django.template import loader

def index(request):
	last_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {
		'last_question_list': last_question_list,
	}
	return HttpResponse(template.render(context, request))
	# or return render(request, 'polls/index.html', context)

def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except:
		raise Http404("Question does not exist")
	return render(request, 'polls/detail.html', {'question':question})
	# or get_object_or_404(Question, pk=question_id)

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." %question_id)
