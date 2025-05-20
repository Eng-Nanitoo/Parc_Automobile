from django.core.mail import send_mail
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages,auth
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q

User = get_user_model()

@login_required
def home(request):
    conducteurs = User.objects.filter(role="CONDUCTEUR")
    notifications = Notification.objects.filter(whom = request.user)
    vehicules = Vehicule.objects.all()
    return render(request, 'home.html', {'vehicules': vehicules,'notifications':notifications,'conducteurs':conducteurs})

@login_required
def addVehicule(request):

    if request.method == "POST":

        vehicule = Vehicule.objects.create(
            image = request.FILES.get('image'),
            marque = request.POST['marque'],
            immatriculation= request.POST['immatriculation'],
            date_achat=  request.POST['date_achat'],
            kilometrage =  request.POST['kilometrage'],
            type_carburant =  request.POST['type_carburant'],
            modele = request.POST['modele']
        )

        vehicule.save()

        return redirect('/home')
    return render(request, '404.html')
@login_required
def modifieVehicule(request, pk):
    vehicule = get_object_or_404(Vehicule, id=pk)

    if request.method == "POST":
        vehicule.marque = request.POST['marque']
        vehicule.modele = request.POST['modele']
        vehicule.immatriculation = request.POST['immatriculation']
        vehicule.date_achat = request.POST['date_achat']
        vehicule.kilometrage = request.POST['kilometrage']
        vehicule.type_carburant = request.POST['type_carburant']
        vehicule.statut = request.POST['statut']

        if request.FILES.get('image'):
            vehicule.image = request.FILES['image']

        vehicule.save()
        return redirect('/vehicules')
    return render(request, '404.html')
@login_required
def deleteVehicule(request, pk):
    if request.method == "GET":
        vehicule = Vehicule.objects.get(id=pk)

        vehicule.delete()

        return render(request , 'vehicules.html')

@login_required
def addUtilisateur(request):
    
    if request.method == "POST":

        Utilisateur = Utilisateur.objects.create_user(
            nom = request.POST['nom'],
            prenom = request.POST['prenom'],
            numero_permis = request.POST['numero_permis'],
            date_validite_permis = request.POST['date_validite_permis'],
            image = request.FILES.get('image'),
        )

        Utilisateur.save()

        return redirect('/Utilisateurs')
    return render(request, '404.html')

@login_required
def modifieUtilisateur(request, pk):
    Utilisateur = get_object_or_404(Utilisateur, id=pk)
    if request.method == "POST":
        Utilisateur.nom = request.POST['nom'],
        Utilisateur.prenom = request.POST['prenom'],
        Utilisateur.numero_permis = request.POST['numero_permis'],
        Utilisateur.date_validite_permis = request.POST['date_validite_permis'],
        Utilisateur.image = request.FILES.get('image')

        if request.FILES.get('image'):
            Utilisateur.image = request.FILES['image']

        Utilisateur.save()
        return redirect('/Utilisateurs')
    
    return render(request, '404.html')

@login_required
def deleteUtilisateur(request, pk):
    if request.method == "GET":
        Utilisateur = get_object_or_404(Utilisateur, id=pk)

        Utilisateur.delete()

        return redirect('/Utilisateurs')
    return render(request, '404.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('/home') 
    return render(request , 'signIn.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('/home') 
    return render(request , 'signUp.html')

def userLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request,username=username, password=password)

        if user is None:

            messages.error(request,"invalid credentials")
            return redirect('/auth/login')
        
        
        auth.login(request,user)

        return redirect('/home')
        
    
    return render(request, '404.html')

def userRegister(request):

    if request.method == "POST":
        username = request.POST['username']
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.filter(Q(username = username) or Q(email=email))

        if user.exists():
            messages.info(request, 'Username or email already used')

            return redirect('/auth/register')
        
        user = User.objects.create_user(username = username, email = email,nom =nom,prenom=prenom)
        user.set_password(password)

        user.save()

        auth.login(request, user)

        return redirect('/home')
    
    return redirect('/auth/register')

def userLogout(request):
    auth.logout(request)
    return redirect('/auth/login')

@login_required
def addPageVehicule(request):
    return render(request, 'addVehicule.html')

@login_required
def addPageUtilisateur(request):
    return render(request, 'addUtilisateur.html')


@login_required
def profile(request, pk):
    return render(request, 'profile.html', {'user' : request.user})


@login_required
def updateProfile(request):
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)

        username = request.POST['username']
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        phone = request.POST['phone']
        email = request.POST['email']
        # password = request.POST['password']

        # user = User.objects.filter(username = username)
        # User.objects.update()

        user.username = username
        user.nom = nom
        user.prenom = prenom
        user.email = email
        # user.password = password
        user.phone = phone

        user.save()

    return redirect(f"/profile/{request.user.username}")