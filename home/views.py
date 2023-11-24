from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    print("you get response")
    return HttpResponse('this is homepage')
