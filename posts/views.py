from django.http import HttpResponse
from django.shortcuts import render

def post_home(request):

	return HttpResponse("<h1>HELLO</h1>")