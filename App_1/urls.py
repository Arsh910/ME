from django.urls import path
from .views import home,Upload_view

app_name='App_1'
urlpatterns=[

    path('',home,name='home'),
    path('upload/',Upload_view,name='upload')

]