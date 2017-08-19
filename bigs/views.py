from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.db import models
from .models import Bigs,Refs
from auth.models import User
from function.functions import get_tree
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from admin.extpaginator import extpaginator
from django.db.models import Q
from .forms import BigsForm,RefsForm
from django.core.urlresolvers import reverse,resolve

# Create your views here.
def index(request):
	p = request.GET.get('p')
	k = request.GET.get('keyword')
	if p == None:
		p = 1
	if k == None:
		k = ''

	if k != '':
		bigs = Bigs.objects.filter(Q(topic__contains=k)|Q(place__contains=k)|Q(roles__contains=k))
	else:
		bigs = Bigs.objects.all()
	paginator = extpaginator(bigs, 10)
	pagestr = paginator.pagestr(p,{'k':k})
	try:
		pbigs = paginator.page(p)
	except PageNotAnInteger:
		pbigs = paginator.page(1)
	except EmptyPage:
		pusers = paginator.page(paginator.num_pages)
	return TemplateResponse(request, 'bigs/index.html',{'bigs':pbigs, 'pagestr':pagestr})

def add(request):
	if request.method == "POST":
		form = BigsForm(request.POST,request.FILES)
		if form.is_valid():
			newBigs = form.save(commit=False)
			newBigs.user = User.objects.get(id=request.session['user_id'])
			try:
				newBigs.save()
			except :
				return HttpResponse('Error')
		return HttpResponseRedirect(reverse('bigs-index'))
	else:
		form = BigsForm()
	return TemplateResponse(request, 'bigs/add.html',{'form':form})

def edit():
	pass

def show():
	pass

def references(request):
	return HttpResponse('references')

def addRefs(request):
	if request.method == "POST":
		form = RefsForm(request.POST,request.FILES)
		if form.is_valid():
			try:
				form.save()
				return HttpResponse('Add Refs Successfully!')
			except :
				return HttpResponse('Error')
	else:
		form = RefsForm()
	return TemplateResponse(request, 'bigs/addRefs.html',{'form':form})
