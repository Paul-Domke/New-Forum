from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import FAQ, Rule
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