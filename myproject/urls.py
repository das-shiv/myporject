from django.contrib import admin
from django.urls import path, include
from myapp import views  # Import views from your app

urlpatterns = [
    # Admin interface
    path('admin/', admin.site.urls),

    # Home page
    path('', views.home, name='home'),

    # User authentication
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in Django authentication views

    # Profile page
    path('profile/', views.profile, name='profile'),
    
    # Sign up page (assuming you've created a view for user signup in your app)
    path('signup/', views.signup, name='signup'),
]

