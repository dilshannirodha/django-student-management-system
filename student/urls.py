from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('add-student/', views.student_add),
    path('delete-student/<slug:regnumber>/',views.student_delete),
    path('update-student/<slug:regnumber>/',views.student_update),
    path('update/<slug:regnumber>/',views.update),
]