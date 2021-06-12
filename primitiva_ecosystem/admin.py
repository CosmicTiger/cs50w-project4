from django.contrib import admin
from .models import Animalia, AnimaliaObservation, AnimaliaLocations, \
    Ecosystem, EcosystemVariations, Plantae, TaxonomicGroup

admin.site.register(Animalia)
admin.site.register(AnimaliaObservation)
admin.site.register(AnimaliaLocations)
admin.site.register(Ecosystem)
admin.site.register(EcosystemVariations)
admin.site.register(Plantae)
admin.site.register(TaxonomicGroup)
