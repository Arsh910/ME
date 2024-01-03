from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Image
from django import forms

# Create your views here.

class Upload_form(forms.Form):
    name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','id':'exampleInputName','placeholder':'Title','style': 'width:80%'}))
    disc=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Discription','style': 'margin:0 0 40px 0; width:80%; font-family:Montserrat, sans-serif; background-color:#EBECF0; text-shadow: 1px 1px 1px #FFF;text-shadow: 1px 1px 0 #FFF;box-shadow:  inset 2px 2px 5px #BABECC, inset -5px -5px 10px #FFF;'}))
    img=forms.FileField()
    def __init__(self, *args, **kwargs):
        super(Upload_form, self).__init__(*args, **kwargs)
        self.fields['img'].widget.attrs.update({'id':'dropzone-file','style':'width:80%'})


def home(requests):
    data=Image.objects.all()
    return render(requests,"home.html",{"data":data})

def Upload_view(requests):
    if requests.method=='POST':
        form=Upload_form(requests.POST,requests.FILES)
        if form.is_valid():
            object=Image.objects.create(
            name=form.cleaned_data['name'],
            disc=form.cleaned_data['disc'],
            img=form.cleaned_data['img'],
            author=requests.user
            )
            object.save()
            return HttpResponseRedirect('/')
        else:
            return render(requests,'upload.html',{'form':form})
    return render(requests,'upload.html',{'form':Upload_form()})
