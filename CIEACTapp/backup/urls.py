from django.conf.urls import  include, url
from django.urls import path
from .views import UploadView#,modelRun

urlpatterns = [
   path('', UploadView, name = 'fileupload'),
   path('', UploadView,name='index'),
   #path('modelsurl', UploadView,name='modelselect'),
   #path('modelsurl', modelRun,name='runmodel'),

  ]