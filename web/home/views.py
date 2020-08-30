from .models import contract
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'home/home.html')

def SCcreator(request):
	return render(request, 'home/home.html')

def postearDummy(request):
	context = {
		'contratos': contract.objects.all()
	}
	return render(request, 'home/dummy.html', context)