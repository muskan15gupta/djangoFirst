from django.urls import path
from . import views 

urlpatterns=[
    path('',views.index,name='index'),
    path('muskan/',views.muskan,name='muskan'),
    path('david/',views.david,name='david'),
    path('<str:name>',views.greet,name='greet'),
    
]