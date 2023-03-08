from django.urls import path
from . import views

urlpatterns = [
    path('', views.label_upload, name='home'),
    path('label/', views.csv_label_upload, name='home'),
    path('ajax_file/',views.csv_upload_temp),
    path('ajax_upload/',views.csv_upload_ajax,name='upload'),
]
