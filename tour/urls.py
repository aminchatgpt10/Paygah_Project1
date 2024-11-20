from django.urls import path
from . import views

app_name = 'tour'
urlpatterns = [
    path('', views.home_view, name='homepage'),
    path('edittour/<int:pk>/', views.edittour, name='edittour'),
    path('add/', views.tour_create, name='add'),
    path('deletetour/<int:pk>/', views.deletetour, name='deletetour')
]
