from django.db import models
from primitiva_project.models import DateRegister
from primitiva_staff.models import PrimitivaOccupations
from primitiva_ecosystem.models import EcosystemVariations, Animalia, Plantae

class ProgramType(models.IntegerChoices):
    INTERNAL_CONTROL = 1, 'Internal Control - Daily checks on the subjects in the natural reserve'
    EXTERNAL_CONTROL = 2, 'External Control - Special checks for investigation or research purposes of external agents from the natural reserve'
    BREEDING_PROGRAM = 3, 'Breeding Program - Programs in which is necessary that certain groups of subject reproduce themselves'
    EMERGENCY_PROGRAM = 4, 'Emergency Program - Programs of contingency when something bad happens in the daily checks'

class GenericStatus(models.IntegerChoices):
    ACTIVE = 1, 'Active - Program or Research is on course'
    PENDING = 2, 'Pending - Program or Research is pending of approval'
    APPROVED = 3, 'Approved - Program or Research is approved'
    DISAPPROVED = 4, 'Disapproved - Program or Research is disapproved for various reasons'
    INACTIVE = 5, 'Inactive - Program or Research is not on course'

class ResearchSubjectStatus(models.IntegerChoices):
    ACTIVE = 1, 'Active - Animal is under research'
    OUT_OF_SIGHT = 2, 'Pending - Animal is out of sight from researchers'
    INACTIVE = 3, 'Inactive - Animal is no longer under research'

class Program(DateRegister):
    program_code = models.CharField(max_length=120, blank=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    program_type = models.IntegerField(choices = ProgramType.choices)
    status = models.IntegerField(choices=GenericStatus.choices)

    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = 'Programs'

class ThreatsBoosters(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    influence = models.IntegerField()

    class Meta:
        verbose_name = 'Threat Booster'
        verbose_name_plural = 'Threat Boosters'
class Threats(models.Model):
    name = models.CharField(max_length=150)
    tendency = models.CharField(max_length=150)
    importance = models.IntegerField()
    boosters = models.ManyToManyField(ThreatsBoosters, through="ThreatsDetails", verbose_name="Threats Details", related_name="threat_details")

    class Meta:
        verbose_name = 'Threat'
        verbose_name_plural = 'Threats'

class ThreatsDetails(models.Model):
    booster = models.ForeignKey(ThreatsBoosters, verbose_name="Boosters", on_delete=models.CASCADE, related_name="boosters")
    threat = models.ForeignKey(Threats, verbose_name="Threat", on_delete=models.CASCADE, related_name="threat")
    effects = models.TextField()

    class Meta:
        verbose_name = 'Threat Detail'
        verbose_name_plural = 'Threat Details'

class ConditionsCauses(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    reasons = models.TextField()

    class Meta:
        verbose_name = 'Condition of the cause'
        verbose_name_plural = 'Conditions of the cause'

class EnvironmentVariables(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    tendency = models.IntegerField()
    causes = models.ManyToManyField(ConditionsCauses, through="EnvironmentVariablesFactors", through_fields=('variable', 'cause'), verbose_name="Causes of Condition", related_name="causes")

    class Meta:
        verbose_name = 'Environment Variable'
        verbose_name_plural = 'Environment Variables'

class EnvironmentVariablesFactors(models.Model):
    variable = models.ForeignKey(EnvironmentVariables, verbose_name="Environment Variables", on_delete=models.CASCADE, related_name="variables")
    cause = models.ForeignKey(ConditionsCauses, verbose_name="Environmental Causes", on_delete=models.CASCADE, related_name="conditions")

    class Meta:
        verbose_name = 'Environment Variable Factor'
        verbose_name_plural = 'Environment Variable Factors'
class EnvironmentVariablesValues(DateRegister):
    variable = models.ForeignKey(EnvironmentVariables, verbose_name="Environment Variables", on_delete=models.CASCADE, related_name="valued_variables")
    morning_value = models.FloatField()
    midday_value = models.FloatField()
    afternoon_value = models.FloatField()
    change_observations = models.TextField()
    register_at = models.DateTimeField()

    class Meta:
        verbose_name = 'Environment Variable Value'
        verbose_name_plural = 'Environment Variable Values'

class Research(DateRegister):
    researcher_lead = models.ForeignKey(PrimitivaOccupations, verbose_name="Researcher Lead", on_delete=models.PROTECT, related_name="researcher_lead")
    program = models.ForeignKey(Program, verbose_name="Program", on_delete=models.CASCADE, related_name="program")
    status = models.IntegerField(choices=GenericStatus.choices)

    class Meta:
        verbose_name = 'Research'
        verbose_name_plural = 'Research List'
class ObservationsResearchEcosystem(models.Model):
    research = models.ForeignKey(Research, verbose_name="Research", on_delete=models.CASCADE, related_name="research_ecosystem")
    variations = models.ForeignKey(EcosystemVariations, verbose_name="Ecosystem Variations", on_delete=models.CASCADE, related_name="variations")
    threats = models.ForeignKey(Threats, verbose_name="Threats on the Ecosystem", on_delete=models.CASCADE, related_name="observed_threats")
    variables = models.ForeignKey(EnvironmentVariables, verbose_name="Environment Variables influencing Ecosystem", on_delete=models.CASCADE, related_name="observed_variables")
    comment = models.TextField()

    class Meta:
        verbose_name = 'Ecosystem Research Observation'
        verbose_name_plural = 'Ecosystem Research Observations'

class ObservationsResearchAnimalia(models.Model):
    research = models.ForeignKey(Research, verbose_name="Research", on_delete=models.CASCADE, related_name="research_animalia")
    researched_animal = models.ForeignKey(Animalia, verbose_name="Researched Animal", on_delete=models.CASCADE, related_name="animalia")
    status = models.IntegerField(choices=ResearchSubjectStatus.choices)
    comment = models.TextField()

    class Meta:
        verbose_name = 'Animal Research Observation'
        verbose_name_plural = 'Animals Research Observations'
class ObservationsResearchPlantae(models.Model):
    research = models.ForeignKey(Research, verbose_name="Research", on_delete=models.CASCADE, related_name="research_plantae")
    researched_plant = models.ForeignKey(Plantae, verbose_name="Researched plant", on_delete=models.CASCADE, related_name="plantae")
    status = models.IntegerField(choices=ResearchSubjectStatus.choices)
    comment = models.TextField()

    class Meta:
        verbose_name = 'Plant Research Observation'
        verbose_name_plural = 'Plants Research Observations'
