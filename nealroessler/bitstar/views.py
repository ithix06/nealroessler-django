from django.shortcuts import render

def index(request):
    welcome_message = "HELLO"
    context = {'welcome_message' : welcome_message}
    return render(request, 'bitstar/index.html', context)
