from django.shortcuts import render
from django.http import HttpResponse
from pt1 import forms

# Create your views here.
def index(request):
    return render(request,'pt1/index.html')

def invbat(request):
    return render(request,'pt1/invbat.html')

def water(request):
    return render(request,'pt1/water.html')

def solar(request):
    return render(request,'pt1/solar.html')

def contact(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            form.save(commit=True)
            dict = {'success' : 'Submitted Successfully..'}
            #return HttpResponse('<h2>Submitted Successfully....</h2>')
            return render(request,'pt1/Contsucc.html')
        else:
            pass
    return render(request,'pt1/contact.html',{'form':form})
