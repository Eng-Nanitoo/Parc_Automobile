import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class Vehicule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    immatriculation = models.CharField(max_length=50, unique=True)
    date_achat = models.DateField()
    kilometrage = models.PositiveIntegerField()
    color = models.CharField(max_length = 20,null=True)
    type_vehicule = models.CharField(max_length = 50)

    TRANSMISSION_CHOICES = [
        ('Automatic','AUTOMATIC' ),
        ('Triptronic','TRIPTRONIC'),
        ('Manual','MANUAL'),
    ]
    VehiculeType_CHOICES = [
        ('Van','Van' ),
        ('Truck','Truck'),
        ('MVP','MVP'),
        ('SUV','SUV'),
        ('Double Cabin','Double Cabin'),
        ('Wagon','Wagon'),
        ('Sedan','Sedan'), 
        ('Hatchback','Hatchback'), 
        ('Coupe','Coupe'), 
        ('Sport','Sport'), 
    ]

    STATUS_CHOICES = [
        ('Disponible', 'DISPONIBLE'),
        ('En maintenance', 'EN_MAINTENANCE'),
        ('En cours d\'utilisation', 'UTILISATION'),
    ]
    type_vehicule = models.CharField(null = True,choices=VehiculeType_CHOICES)
    transmission = models.CharField(max_length=50,choices=TRANSMISSION_CHOICES,null=True)
    type_carburant = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'vehicules_images')
    

    statut = models.CharField(max_length=50, choices=STATUS_CHOICES, default='DISPONIBLE')

    def __str__(self):
        return self.marque + " " + self.modele

class Utilisateur(AbstractUser):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    numero_permis = models.CharField(max_length=50, unique=True, null=True)
    date_validite_permis = models.DateField(null=True)
    date_creation = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to = 'users_profiles' , default="users_profiles/user.jpg")
    phone = models.CharField(max_length=8, null=True)

    ROLE_CHOICES = [
        ('CONDUCTEUR', 'Conducteur'),
        ('GESTIONNAIRE', 'Gestionnaire'),
        ('ADMIN', 'Admin'),
    ]
    canDrive = models.BooleanField(default=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES,default="CONDUCTEUR")

class Trajet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    Utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date_depart = models.DateTimeField()
    date_arrivee = models.DateTimeField()
    kilometrage_parcouru = models.PositiveIntegerField()
    consommation_carburant = models.FloatField(help_text="Consommation en litres")

class Maintenance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date = models.DateField()
    type_maintenance = models.CharField(max_length=100)
    cout = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)


class Depense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    CATEGORIE_CHOICES = [
        ('CARBURANT', 'Carburant'),
        ('MAINTENANCE', 'Maintenance'),
        ('ASSURANCE', 'Assurance'),
        ('PEAGE', 'Péage'),
    ]
    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_depense = models.DateField()
    description = models.TextField(blank=True)

class Notification(models.Model):
    whom = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    description = models.TextField()
    when = models.DateTimeField(auto_now_add=True)
