from django.shortcuts import render
from .models import profile
from django.http import HttpResponseRedirect,JsonResponse
from App_1.models import Image 
from django import forms
from django.contrib.auth.decorators import login_required



class Edit_form(forms.Form):
    name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','id':'exampleInputName','placeholder':'NAME','style': 'width:80%'}))
    bio=forms.CharField(max_length=240,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'BIO','style': 'margin:0 0 40px 0; width:80%; font-family:Montserrat, sans-serif; background-color:#EBECF0; text-shadow: 1px 1px 1px #FFF;text-shadow: 1px 1px 0 #FFF;box-shadow:  inset 2px 2px 5px #BABECC, inset -5px -5px 10px #FFF;'}))
    image=forms.FileField()
    def __init__(self, *args, **kwargs):
        super(Edit_form, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'id':'dropzone-file','style':'width:80%'})
    
# Create your views here.
def Prof(requests,pk,user):
    
    d=Image.objects.filter(id=pk)
    d_cou=Image.objects.filter(id=pk).count()
    da=profile.objects.filter(user_id=pk)
    print(da)
    return render(requests,"profile.html",{"da":da,"d":d,"total":d_cou})

@login_required

def edit_form(requests,pk,user):
    if requests.method=='POST':
        form = Edit_form(requests.POST,requests.FILES)
        if form.is_valid():
            object = profile.objects.get(user_id=pk)
            object.name=form.cleaned_data['name']
            object.bio=form.cleaned_data['bio']
            
            if 'image' in requests.FILES:
                object.image=requests.FILES['image']
            object.save()
            return HttpResponseRedirect(f'/profile/{pk}/{user}')
        else:
            return render(requests,"edit_prof.html",{"form" : form})
    else:   
        return render(requests,"edit_prof.html",{"form" : Edit_form()}) 