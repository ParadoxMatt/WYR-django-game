from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
import random
# Create your views here.
from .models import Scenario, Category

# Create your views here.
class Index(generic.View):
    template_name = "WYR/index.html" 
    
class SCQView(generic.DetailView):
    model = Scenario
    category_filter = Category
    template_name = "WYR/SCQ.html"

class VotesView(generic.DetailView):
    model = Scenario
    template_name = "WYR/votes.html"


def votes(request, scenario_id):

    question = get_object_or_404(Scenario, pk=scenario_id)
    try:
        selected = request.POST["choice"]
    except (KeyError):
        return render(
            request,
            "WYR/SCQ.html",
            {
                "option_1":question.scenario_question_1,
                "option_2":question.scenario_question_2,

                "error_message":"Select a proper option"
            },
        )
    else:
        if selected == "1":
            question.votesQ1 +=1
            question.save()
        else:
            question.votesQ2 +=1
            question.save()
    
    return HttpResponseRedirect(reverse("WYR:votes", args=(question.id),))