# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from rest_framework import serializers


class MmsCmpnt(models.Model):
    cmpny_id = models.CharField(max_length=20)
    eqp_sn = models.IntegerField()
    cmpnt_sn = models.AutoField(primary_key=True)
    equippart_cd = models.CharField(max_length=10, blank=True, null=True)
    cmpnt_nm = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MMS_CMPNT'


class MmsEqp(models.Model):
    cmpny_id = models.CharField(max_length=20)
    eqp_sn = models.AutoField(primary_key=True)
    procs_cd = models.CharField(max_length=10, blank=True, null=True)
    eqpty_cd = models.CharField(max_length=10, blank=True, null=True)
    eqp_nm = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MMS_EQP'


class MmsImprmn(models.Model):
    cmpny_id = models.CharField(max_length=20, verbose_name='회사코드')
    eqp_sn = models.IntegerField(verbose_name='설비')
    cmpnt_sn = models.IntegerField(blank=True, null=True, verbose_name='부품')
    imprmn_sn = models.AutoField(primary_key=True)
    presvse_cd = models.CharField(max_length=10, blank=True, null=True, verbose_name='보전구분')
    presvexecut_cd = models.CharField(max_length=10, blank=True, null=True, verbose_name='보전실행')
    opertdept_cd = models.CharField(max_length=10, blank=True, null=True, verbose_name='작업부서')
    chckat_cd = models.CharField(max_length=10, blank=True, null=True, verbose_name='점검여부')
    nrmltat_cd = models.CharField(max_length=10, blank=True, null=True, verbose_name='정상여부')
    processdept_cd = models.CharField(max_length=10, blank=True, null=True, verbose_name='처리주체')
    opertse_cd = models.CharField(max_length=10, blank=True, null=True, verbose_name='작업구분')
    defectsittn_cd = models.CharField(max_length=10, blank=True, null=True, verbose_name='고장상황')
    defectcause_cd = models.CharField(max_length=10, blank=True, null=True, verbose_name='고장원인')
    chck_de = models.CharField(max_length=8, blank=True, null=True, verbose_name='점검일자')
    opert_cn = models.CharField(max_length=1000, blank=True, null=True, verbose_name='작업내용')
    opert_user_id = models.CharField(max_length=20, blank=True, null=True, verbose_name='작업자')
    begin_dt = models.CharField(max_length=20, blank=True, null=True, verbose_name='시작일시')
    end_dt = models.CharField(max_length=20, blank=True, null=True, verbose_name='종료일시')


    class Meta:
        managed = False
        db_table = 'MMS_IMPRMN'

    def __str__(self):
        return self.imprmn_sn

class MmsImprmnSerializer(serializers.ModelSerializer):
    class Meta:
        model = MmsImprmn
        fields = '__all__'

    def create(self, validated_data):
        return MmsImprmn.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.cmpny_id = validated_data.get('cmpny_id', instance.cmpny_id)
        instance.eqp_sn = validated_data.get('eqp_sn', instance.eqp_sn)
        instance.presvse_cd = validated_data.get('presvse_cd', instance.presvse_cd)
        instance.presvexecut_cd = validated_data.get('presvexecut_cd', instance.presvexecut_cd)
        instance.opertdept_cd = validated_data.get('opertdept_cd', instance.opertdept_cd)
        instance.chckat_cd = validated_data.get('chckat_cd', instance.chckat_cd)
        instance.nrmltat_cd = validated_data.get('nrmltat_cd', instance.nrmltat_cd)
        instance.processdept_cd = validated_data.get('processdept_cd', instance.processdept_cd)
        instance.opertse_cd = validated_data.get('opertse_cd', instance.opertse_cd)
        instance.defectsittn_cd = validated_data.get('defectsittn_cd', instance.defectsittn_cd)
        instance.defectcause_cd = validated_data.get('defectcause_cd', instance.defectcause_cd)
        instance.chck_de = validated_data.get('chck_de', instance.chck_de)
        instance.opert_cn = validated_data.get('opert_cn', instance.opert_cn)
        instance.opert_user_id = validated_data.get('opert_user_id', instance.opert_user_id)
        instance.begin_dt = validated_data.get('begin_dt', instance.begin_dt)
        instance.end_dt = validated_data.get('end_dt', instance.end_dt)
        instance.cmpnt_sn = validated_data.get('cmpnt_sn', instance.cmpnt_sn)

        instance.save()
        return instance


class MmsPresv(models.Model):
    eqp_sn = models.IntegerField()
    cmpny_id = models.CharField(max_length=20)
    presvpd_day = models.CharField(max_length=10, blank=True, null=True)
    stdrpresv_de = models.CharField(max_length=8, blank=True, null=True)
    cmpnt_sn = models.IntegerField(blank=True, null=True)
    presv_sn = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'MMS_PRESV'


class SysCmmncdD(models.Model):
    mcode_id = models.CharField(max_length=10)
    dcode_nm = models.CharField(max_length=50, blank=True, null=True)
    dcode_val1 = models.CharField(max_length=100, blank=True, null=True)
    dcode_val2 = models.CharField(max_length=100, blank=True, null=True)
    dcode_val3 = models.CharField(max_length=100, blank=True, null=True)
    ord_seq = models.IntegerField(blank=True, null=True)
    cmpny_id = models.CharField(max_length=20)
    dcode_sn = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'SYS_CMMNCD_D'

    def __str__(self):
        return self.dcode_nm

class SysCmmncdDSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysCmmncdD
        fields = '__all__'

    def create(self, validated_data):
        return SysCmmncdD.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.cmpny_id = validated_data.get('cmpny_id', instance.cmpny_id)
        instance.mcode_id = validated_data.get('mcode_id', instance.mcode_id)
        instance.dcode_nm = validated_data.get('dcode_nm', instance.dcode_nm)
        instance.dcode_val1 = validated_data.get('dcode_val1', instance.dcode_val1)
        instance.dcode_val2 = validated_data.get('dcode_val2', instance.dcode_val2)
        instance.dcode_val3 = validated_data.get('dcode_val3', instance.dcode_val3)
        instance.ord_seq = validated_data.get('ord_seq', instance.ord_seq)

        instance.save()
        return instance

class SysCmmncdM(models.Model):
    MCODE_CHOICES = (('MMS', 'MMS'), ('SYS', 'SYS'))

    mcode_id = models.CharField(primary_key=True, max_length=10, verbose_name='코드ID')
    mcode_cd = models.CharField(max_length=20, blank=True, null=True, verbose_name='코드CD', choices=MCODE_CHOICES, default='MMS')
    mcode_nm = models.CharField(max_length=50, blank=True, null=True, verbose_name='코드명')
    auth_cd = models.CharField(max_length=10, blank=True, null=True, verbose_name='권한코드')

    class Meta:
        ordering = ('mcode_id',)
        verbose_name_plural = '공통코드 마스터'
        verbose_name = '공통코드'
        managed = False
        db_table = 'SYS_CMMNCD_M'

    def __str__(self):
        return '공통코드: {}'.format(self.mcode_id)


class SysMngr(models.Model):
    mngr_id = models.CharField(primary_key=True, max_length=20)
    mngr_nm = models.CharField(max_length=50, blank=True, null=True)
    auth_cd = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SYS_MNGR'


class UsrCmpny(models.Model):
    cmpny_id = models.CharField(primary_key=True, max_length=20, verbose_name='회사코드')
    cmpny_nm = models.CharField(max_length=100, blank=True, null=True, verbose_name='회사명')
    cmpny_tlphon = models.CharField(max_length=20, blank=True, null=True, verbose_name='회사전화')
    cmpny_adres1 = models.CharField(max_length=200, blank=True, null=True, verbose_name='회사주소')
    charger_nm = models.CharField(max_length=20, blank=True, null=True, verbose_name='담당자명')
    charge_moblphon = models.CharField(max_length=20, blank=True, null=True, verbose_name='담당자 핸드폰')


    class Meta:
        ordering = ('cmpny_id',)
        verbose_name_plural = '회사'
        verbose_name = '회사'
        managed = False
        db_table = 'USR_CMPNY'

    def __str__(self):
        return '회사: {}'.format(self.cmpny_nm)



class UtlCldr(models.Model):
    cldr_de = models.CharField(max_length=8)
    cldr_cn = models.CharField(max_length=1000, blank=True, null=True)
    cmpny_id = models.CharField(primary_key=True, max_length=20)
    cldrse_cd = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UTL_CLDR'
        unique_together = (('cmpny_id', 'cldr_de'),)
