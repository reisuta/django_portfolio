from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'web/index.html')

def detail(request, wrie):
    return render(request, 'web/detail.html')