# Generated by Django 3.2.4 on 2021-06-11 04:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('primitiva_ecosystem', '0001_initial'),
        ('primitiva_staff', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='User Authentication'),
        ),
        migrations.AddField(
            model_name='primitivaoccupations',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role', to='primitiva_staff.primitivarole', verbose_name='Primitiva Member Role'),
        ),
        migrations.AddField(
            model_name='primitivaoccupations',
            name='specialty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='specialty', to='primitiva_ecosystem.taxonomicgroup', verbose_name='Primitiva Specialty'),
        ),
        migrations.AddField(
            model_name='primitivaoccupations',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='primitiva_staff.staff', verbose_name='Primitiva Staff Member'),
        ),
    ]
