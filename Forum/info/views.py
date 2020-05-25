from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from .models import FAQ, Rule, HoursOfOp
from posts.models import Tag
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DetailView,
)
from users.models import Profile
from django.template import RequestContext

# Create your views here.

class FAQListView(LoginRequiredMixin, ListView):
	model = FAQ
	context_object_name = 'FAQs'

class RulesListView(LoginRequiredMixin, ListView):
	model = Rule
	context_object_name = 'rules'

def rules(request):
	context={
		'rules': Rule.objects.all(),
		'tags': Tag.objects.all(),
	}
	return render(request, 'info/rule_list.html', context)

class FAQCreateView(LoginRequiredMixin, CreateView):
	model = FAQ
	fields = ['question', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class RuleCreateView(LoginRequiredMixin, CreateView):
	model = Rule
	fields = ['rule', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

#class HoursOfOperationListView(LoginRequiredMixin, ListView):
#	model = HoursOfOp
#	context_object_name = 'hoursOfOp'

def hoursOfOperation(request):

	context={
		'service': HoursOfOp.objects.all(),
		'tags': Tag.objects.all(),
	}
	return render(request, 'info/hoursofop_list.html', context)
	