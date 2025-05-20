from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.core.mail import send_mail

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