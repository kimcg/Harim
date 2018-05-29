from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sysCmmncdD/', views.sysCmmncdD, name='sysCmmncdD'),
    path('sysCmmncdD_List/', views.sysCmmncdD_List, name='sysCmmncdD_List'),
    path('sysCmmncdD_Save/', views.sysCmmncdD_Save, name='sysCmmncdD_Save'),

    path('mmsImprmn/', views.mmsImprmn, name='mmsImprmn'),
    path('mmsImprmnForm/', views.mmsImprmnForm, name='mmsImprmnForm'),
    path('mmsImprmnForm2/', views.mmsImprmnForm2, name='mmsImprmnForm2'),
    path('mmsImprmn_List/', views.mmsImprmn_List, name='mmsImprmn_List'),
    path('mmsImprmn_Save/', views.mmsImprmn_Save, name='mmsImprmn_Save'),

    path('load_cmpnts/', views.load_cmpnts, name='load_cmpnts'),


    path('chart/', views.chart, name='chart'),

]