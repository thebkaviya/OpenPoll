import datetime

from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.TemplateView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'


def detail(request, _id):
    try:
        question = Question.objects.get(id=_id)
    except (KeyError, Question.DoesNotExist):
        # Display an Poll doesn't exist page
        return render(request, 'polls/poll_error.html', {'error': {
            'head': "HMM.",
            'body': "we can't find any poll with that ID",
            'code': "404_Poll_Not_Found",
            'title': "Poll Not Found"
        }})
    else:
        if question.voting_closed:
            return render(request, 'polls/poll_error.html', {'error': {
                'head': "WELL THAT SUCKS.",
                'body': "the poll you're looking for is closed",
                'code': "Poll_Closed",
                'title': "Poll Closed"
            }})
        elif question.enable_closed_date and question.is_expired():
            return render(request, 'polls/poll_error.html', {'error': {
                'head': "OOPS.",
                'body': "the poll you're looking for has expired",
                'code': "Poll_Expired",
                'title': "Poll Expired"
            }})
        return render(request, 'polls/detail.html', {'question': question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if question.voting_closed or question.is_expired():
        return HttpResponseNotFound()
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
