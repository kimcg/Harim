from django.contrib import admin
from suit.admin import RelatedFieldAdmin, get_related_field
from suit.sortables import SortableTabularInline, SortableModelAdmin, SortableStackedInline
from .models import *

# Register your models here.

admin.site.site_header = 'Harim'


@admin.register(SysCmmncdM)
class SysCmmncdMAdmin(RelatedFieldAdmin):
    list_display = ('mcode_id', 'mcode_nm', 'mcode_cd', 'auth_cd')

@admin.register(UsrCmpny)
class UsrCmpnyAdmin(RelatedFieldAdmin):
    list_display = ('cmpny_id', 'cmpny_nm', 'cmpny_tlphon', 'cmpny_adres1', 'charger_nm', 'charge_moblphon')

