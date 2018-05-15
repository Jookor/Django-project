from django.urls import path
from caseHandler import views

app_name = 'caseHandler'

urlpatterns = [
    path('',views.index,name="index"),
    path('case/', views.case,name='case'),
    path('open/',views.open,name='open'),
    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative'),
]
