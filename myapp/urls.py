
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('result/',views.student_result,name='result'),
    path('details/<int:chai_id>/', views.student_detail, name='detail'),
]
