from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse('Ваш водитель Умер ക')	

def momo(request):
	return HttpResponse('Уходите.')		