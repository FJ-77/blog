from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request ,'posts/index.html')	

def user_list(request):
	return HttpResponse('<p>Пользователи:</p>Андрей')	