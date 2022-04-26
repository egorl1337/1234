from django.shortcuts import render

# Create your views here.

def index(request):
    data = {'name':'Главная страница', 'test':[1, 2, 3, 'test', 'weqret'], 'test2':{'test':'123'}}
    return render(request, 'e\index.html', data)

def about(request):
    return render(request, 'e/about.html')

