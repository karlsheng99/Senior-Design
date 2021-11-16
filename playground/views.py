from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def daily_summary(request):
    return render(request, 'pie2.html')

def task_list(request):
    return HttpResponse('tasks')

def test(request):
    return render(request, 'test1.html')
