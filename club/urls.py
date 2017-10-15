from django.conf.urls import url

from . import views

urlpatterns = [
    #url('^home/', views.home, name='home'),
    url('^other/', views.other, name='other'),
    url('^', views.index, name='index'),
]
