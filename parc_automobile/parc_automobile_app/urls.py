from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('profile/<str:pk>', views.profile),
    path('update/profile', views.updateProfile),
    
    path('auth/login', views.login),
    path('auth/register', views.register),
    path('user/auth/login', views.userLogin),
    path('user/auth/register', views.userRegister),

    path('ajouter/vehicule', views.addPageVehicule),
    path('ajouter/Utilisateur', views.addPageUtilisateur),

    path('vehicules/add', views.addVehicule),
    path('vehicules/delete/<int:pk>', views.deleteVehicule),
    path('vehicules/modifie/<int:pk>', views.modifieVehicule),

    path('Utilisateurs/add', views.addUtilisateur),
    path('Utilisateurs/delete/<int:pk>', views.deleteUtilisateur),
    path('Utilisateurs/modifie/<int:pk>', views.modifieUtilisateur),

    path('auth/logout', views.userLogout),
]