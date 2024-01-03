from django.urls import path
from .views import Prof,edit_form

app='prof'

urlpatterns=[
    path('profile/<int:pk>/<str:user>/',Prof, name='profile_data'),
    path('<int:pk>/<str:user>/edit_prof/',edit_form,name='edit_form'),
]
