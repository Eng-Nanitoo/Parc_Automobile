# Generated by Django 5.2 on 2025-05-12 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parc_automobile_app', '0005_alter_vehicule_statut'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='phone',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
