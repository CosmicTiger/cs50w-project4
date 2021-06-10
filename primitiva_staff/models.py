from django.db import models
from primitiva_project.models import DateRegister
from primitiva_ecosystem.models import TaxonomicGroup
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

class PrimitivaRole(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

class Staff(DateRegister):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="User Authentication", on_delete=models.PROTECT, related_name="user")
    primitiva_code = models.CharField(max_length=150)
    identification_photo = models.ImageField(upload_to="staff_media/", verbose_name="photo")
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    secondary_last_name = models.CharField(max_length=150)
    profession = models.CharField(max_length=150)
    address = models.TextField()
    phone = models.CharField(max_length=150)
    residence_city = models.CharField(max_length=150)
    occupation = models.ManyToManyField(PrimitivaRole, through="PrimitivaOccupations", through_fields=('staff', 'role'), verbose_name="Primitiva Occupation", related_name="occupation")
    specialty = models.ManyToManyField(TaxonomicGroup, through="TaxonomicGroup", through_fields=('staff', 'specialty'), verbose_name="Specialty in Taxonomic Groups", related_name="specialty")

class PrimitivaOccupations(models.Model):
    staff = models.ForeignKey(Staff, verbose_name="Primitiva Staff Member", on_delete=models.CASCADE, related_name="staff")
    role = models.ForeignKey(PrimitivaRole, verbose_name="Primitiva Member Role", on_delete=models.CASCADE, related_name="role")
    specialty = models.ForeignKey(TaxonomicGroup, verbose_name="Primitiva Specialty", on_delete=models.CASCADE, related_name="specialty", null=True)
