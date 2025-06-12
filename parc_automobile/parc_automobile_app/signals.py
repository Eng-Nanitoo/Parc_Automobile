from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.core.mail import send_mail
from django.utils.timezone import now
from django.contrib import messages
from .models import *

User = get_user_model()

@receiver(post_save, sender=User)
def send_user_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Welcome to My Site!',
            'Mere7be bik!',
            'nani280224@gmail.com',
            [f"{instance.email}"],
            fail_silently = False,
        )


@receiver(post_save, sender=Maintenance)
def change_vehicule_status(sender, instance, created, **kwargs):
    vehicule = instance.vehicule
    depense = Depense.objects.create(vehicule=vehicule,categorie=instance.type_maintenance,montant=instance.cout,date_depense=instance.date,description=instance.description)
    depense.save()

    vehicule.statut = "En maintenance"
    vehicule.save()

@receiver(user_logged_in)
def check_permis_validate(sender, request, user, **kwargs):
    if hasattr(user, 'date_validite_permis') and user.date_validite_permis:
        today = now().date()
        days = (user.date_validite_permis - today).days

        if 0 <= days <= 30:
            messages.warning(
                request,
                f"Votre permis expire dans {days} jour(s). Veuillez le renouveler bientôt."
            )

            if days <= 5 and not Notification.objects.filter(
                whom=user,
                when=today
            ).exists():
                Notification.objects.create(
                    whom=user,
                    type="Expire Permis",
                    description=f"Bienvenue {user.nom}, votre permis expire dans {days} jour(s).",
                    when=today
                )

        elif days < 0:
            messages.error(
                request,
                "Votre permis a expiré ! Veuillez le renouveler immédiatement."
            )

            if not Notification.objects.filter(
                whom=user,
                when=today
            ).exists():
                Notification.objects.create(
                    whom=user,
                    type="Expire Permis",
                    description=f"Bienvenue {user.nom}, votre permis a expiré.",
                    when=today
                )

