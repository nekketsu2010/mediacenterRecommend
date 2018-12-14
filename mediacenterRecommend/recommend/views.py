from django.shortcuts import render
from django import forms
from . import mediacenter
from . import mecab

# Create your views here.
class Form(forms.Form):
    id = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

def post_list(request):
    if request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']
        mediacenter.scroll(id, password)
        mecab.readCSV(id)
        return render(request, 'recommend/ok.html', {})
    else:
        f = Form()
        return render(request, 'recommend/post_list.html', {'form': f})
