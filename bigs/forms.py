from django import forms
from django.forms import ModelForm
from bigs.models import Bigs,Refs

class BigsForm(ModelForm):

	class Meta:
		model = Bigs
		fields = ['id','topic','year','date','era','place','roles','content','refs','memo','image']

class RefsForm(ModelForm):

	class Meta:
		model = Refs
		fields = ['id','name','author','publisher','pubtime','cover','intro']
