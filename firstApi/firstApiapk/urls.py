from django.contrib import admin
from django.urls import path,include
from firstApiapk import views

urlpatterns = [
     path('admin/', admin.site.urls),
     path('stuinfo/<int:pk>/', views.student_detail),
     path('stuinfo/', views.student_detail),
     # path('stulist/', views.studen_list),
]