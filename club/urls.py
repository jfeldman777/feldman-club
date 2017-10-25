from django.conf.urls import url

from . import views

urlpatterns = [
    url('^quiz_table/', views.quiz_table, name='quiz_table'),
    url('^map/', views.map, name='map'),
    url('^news/', views.news, name='news'),
    url('^other/', views.other, name='other'),
    url('^', views.index, name='index'),
]
