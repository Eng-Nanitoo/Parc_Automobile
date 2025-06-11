from django.urls import path
from . import views


urlpatterns = [
    # Pages paths
    path('rapport/<int:annee>/<int:mois>', views.rapport_mensuel),
    path('home/', views.home),
    path('dashbord/', views.dashbord),
    path('profile/<str:pk>', views.profile),
    path('update/profile', views.updateProfile),
    path('vehicule/<str:pk>', views.getVehicule),
    path('conducteurs/', views.conducteurs),
    path('rapport/excel/<int:mois>/<int:annee>', views.export_excel),
    path('rapport/word/<int:mois>/<int:annee>', views.export_word),
    path('rapport/annuel', views.rapport_annuel_page),
    path('rapport/<int:annee>/excel/', views.export_rapport_annuel_excel, name='rapport_annuel_excel'),
    path('rapport/<int:annee>/word/', views.export_rapport_annuel_word, name='rapport_annuel_word'),
    path('vehicule/<str:pk>', views.getVehicule),

    # User register and login paths
    path('auth/login', views.login),
    path('auth/register', views.register),
    path('user/auth/login', views.userLogin),
    path('user/auth/register', views.userRegister),

    path('ajouter/vehicule', views.addPageVehicule),
    path('ajouter/conducteur', views.addPageUtilisateur),

    # CRUD on vehicules and conducters paths
    path('vehicules/add', views.addVehicule),
    path('vehicules/delete/<int:pk>', views.deleteVehicule),
    path('vehicules/modifie/<str:pk>', views.modifieVehicule),

    path('Utilisateurs/add', views.addConducteur),
    path('Utilisateurs/delete/<int:pk>', views.deleteConducteur),
    path('Utilisateurs/modifie/<int:pk>', views.modifieConducteur),

    path('Programmer/maintenance', views.programmerMaintenance),
    path('ajouter/maintenance', views.addMaintenance),

    # User logout path
    path('auth/logout', views.userLogout),
]