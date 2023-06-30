from django.urls import path
from messageapp import views
urlpatterns = [
   path('student',views.student),
   path('registration',views.registration),
   path('delete/<rid>',views.delete),
   path('edit/<rid>',views.delete),
   
]   