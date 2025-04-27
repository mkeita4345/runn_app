# users/urls.py
# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),  # <-- ADD THIS
    path('diet/', views.diet_page, name='diet_page'),
    path('run_tracking/', views.run_tracking_page, name='run_tracking_page'),
    path('connect/', views.connect_page, name='connect_page'),
    path('diet/', views.diet_view, name='diet_view'),
    path('get_meals/', views.get_meals, name='get_meals'),  # Add URL for get_meals
    path('add_meal/', views.add_meal, name='add_meal'),  # Add URL for add_meal
    path('delete_meal/', views.delete_meal, name='delete_meal'),
]

