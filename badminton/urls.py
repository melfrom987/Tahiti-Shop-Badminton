"""
URL configuration for badminton project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from badminton import views as badminton_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', badminton_views.home, name='home'),  # Page d'accueil
    path('inventory/', include('inventory.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Chemin pour la connexion
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Ajout pour la déconnexion
    path('accounts/signup/', views.signup, name='signup'), #Creation user
    path('home_private/', badminton_views.home_private, name='home_private'),
    path('profile/', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)