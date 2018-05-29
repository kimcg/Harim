from django.contrib import admin
from suit.admin import RelatedFieldAdmin
from .models import *


# Register your models here.
@admin.register(UsrUser)
class UsrUserAdmin(RelatedFieldAdmin):
    list_display = ('user_id', 'user_nm', 'dept_cd', 'clsf_cd')