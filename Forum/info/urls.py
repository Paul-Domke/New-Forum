from django.urls import path
from . import views
from users import views as user_views
from .views import (
	FAQListView,
	RulesListView,
	FAQCreateView,
	RuleCreateView,
	)

urlpatterns = [
    path('info/rules', views.rules, name='info-rules'),
    path('info/FAQ', FAQListView.as_view(), name='info-FAQ'),
    path('info/hoursOfOperation',views.hoursOfOperation, name='info-hours'),
]