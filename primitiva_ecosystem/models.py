from django.db import models
from primitiva_project.models import DateRegister
from django.utils import timezone

class TaxonomicStatus(models.IntegerChoices):
    # Low Risk
    LC = 0, 'LC - Preocupación menor'
    NT = 1, 'NT - Casi amenazada'
    # In Risk
    VU = 2, 'VU - Vulnerable'
    EN = 3, 'EN - En peligro'
    CR = 4, 'CR - En peligro crítico'
    # Extinct
    EW = 5, 'EW - Extinta en estado silvestre'
    EX = 6, 'EX - Extinta'


# Create your models here.
class TaxonomicGroup(models.Model):
    common_name = models.CharField(max_length=150, blank=False)
    family = models.CharField(max_length=150, blank=False)
    cientific_name = models.CharField(max_length=150, blank=False)
    status = models.IntegerField(choices=TaxonomicStatus.choices)

    def __str__(self):
        return f"Family: {self.family} - Common Name: {self.common_name} - Cientific Name: {self.cientific_name} - Status: {self.status}"

    class Meta:
        # db_table = 'taxonomic_groups'
        verbose_name = 'Taxonomic Group'
        verbose_name_plural = 'Taxonomic Groups'

class Sex(models.IntegerChoices):
    MALE = 1, 'M - Male subject'
    FEMALE = 2, 'F - Female subject'

class AnimaliaStatus(models.IntegerChoices):
    DECEASED = 1, 'Deceased - Subject died for natural causes'
    DECEASED_HUMAN = 2, 'Deceased by human - Subject died due to human sources'
    SICK = 3, 'Sick - Subject is sick and observated by caretakers'
    CRIPPLED = 4, "Crippled - Subject is healthy but have certain conditions that doesn't allow it to live normally"
    HEALTHY = 5, 'Healthy - Subject is healthy and good conditions'
    IN_HEAT = 6, 'In heat - Subject is in heat trying to copulate'
    PREGNANT = 7, 'Pregnant - Female subject in pregnancy'


class Animalia(DateRegister):
    animalia_code = models.CharField(max_length=20, unique=True)
    taxonomic_group = models.ForeignKey(TaxonomicGroup, verbose_name="Taxonomic Group", on_delete=models.CASCADE, related_name="group")
    primitiva_name = models.CharField(max_length=150)
    procedence = models.CharField(max_length=500)
    age = models.IntegerField()
    sex = models.IntegerField(choices=Sex.choices)
    status = models.IntegerField(choices=AnimaliaStatus.choices)

    def __str__(self):
        return f"Animal code: {self.animalia_code} -\ Taxonomic Group where belongs: {self.taxonomic_group} -\
            Animal name: {self.primitiva_name} - Procedence: {self.procedence} - Age: {self.age} - Sex: {self.sex} - Status: {self.status}"

    class Meta:
        # db_table = 'animalia'
        verbose_name = 'Animal'
        verbose_name_plural = 'Animals'

class AnimaliaObservation(models.Model):
    animalia = models.ForeignKey(Animalia, verbose_name="Subject", on_delete=models.CASCADE, related_name="animal_subject")
    characteristics = models.TextField()
    natural_performance = models.TextField()
    overall_size = models.FloatField()
    head_size = models.FloatField()
    body_size = models.FloatField()
    extremities_size = models.FloatField()
    overall_weight = models.FloatField()
    head_weight = models.FloatField()
    body_weight = models.FloatField()
    extremities_weight = models.FloatField()
    subject_evolution = models.TextField()
    current_status = models.IntegerField(choices=AnimaliaStatus.choices)
    symptoms = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Animal Observation'
        verbose_name_plural = 'Animal Observations'

class AnimaliaLocations(models.Model):
    animalia = models.ForeignKey(Animalia, verbose_name="Subject", on_delete=models.CASCADE, related_name="subject")
    natural_location = models.CharField(max_length=150)
    latitude = models.FloatField()
    longitude = models.FloatField()
    date_witnessed = models.DateTimeField()

    class Meta:
        verbose_name = 'Animal Location'
        verbose_name_plural = 'Animal Locations'

class Plantae(DateRegister):
    plantae_code = models.CharField(max_length=20, unique=True)
    taxonomic_group = models.ForeignKey(TaxonomicGroup, verbose_name="Taxonomic Group", on_delete=models.CASCADE, related_name="specie")
    primitiva_name = models.CharField(max_length=150)
    procedence = models.CharField(max_length=500)
    age = models.IntegerField()
    sex = models.IntegerField(choices=Sex.choices)
    size = models.FloatField()
    weight = models.FloatField()

    class Meta:
        verbose_name = 'Plant'
        verbose_name_plural = 'Plants'

class Ecosystem(models.Model):
    name = models.CharField(max_length=150)
    variations = models.IntegerField()

    class Meta:
        verbose_name = 'Ecosystem'
        verbose_name_plural = 'Ecosystems'

class EcosystemVariations(models.Model):
    main_ecosystem = models.ForeignKey(Ecosystem, verbose_name="Main ecosystem", on_delete=models.CASCADE, related_name="main")
    sub_ecosystem = models.ForeignKey(Ecosystem, verbose_name="Sub ecosystem", on_delete=models.CASCADE, related_name="sub")
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Ecosystem Variation'
        verbose_name_plural = 'Ecosystem Variations'
