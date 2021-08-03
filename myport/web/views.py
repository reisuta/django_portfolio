from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'web/base.html')

def detail(request, write):
    return render(request, 'web/detail.html')

def test(request):
    return render(request, 'web/test.html')