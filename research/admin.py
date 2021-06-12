from django.contrib import admin
from .models import ObservationsResearchAnimalia, ObservationsResearchPlantae, Program, ThreatsBoosters, \
    Threats, ThreatsDetails, ConditionsCauses, \
    EnvironmentVariables, EnvironmentVariablesFactors, \
    EnvironmentVariablesValues, Research, ObservationsResearchEcosystem \

admin.site.register(Threats)
admin.site.register(ThreatsBoosters)
admin.site.register(ThreatsDetails)
admin.site.register(ConditionsCauses)
admin.site.register(EnvironmentVariables)
admin.site.register(EnvironmentVariablesFactors)
admin.site.register(EnvironmentVariablesValues)
admin.site.register(Program)
admin.site.register(Research)
admin.site.register(ObservationsResearchAnimalia)
admin.site.register(ObservationsResearchPlantae)
admin.site.register(ObservationsResearchEcosystem)
