from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {'text':'hello world', 'number':100}
    return render(request,'caseHandler/index.html',context_dict)

def case(request):
    return render(request,'caseHandler/case.html')

def open(request):
    return render(request,'caseHandler/open.html')

def other(request):
    return render(request,'caseHandler/other.html')

def relative(request):
    return render(request,'caseHandler/relative_url_templates.html')
