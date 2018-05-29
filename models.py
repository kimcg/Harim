# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    cmpny_id = models.CharField(max_length=20)
    eqp_sn = models.IntegerField()
    imprmn_sn = models.AutoField(primary_key=True)
    presvse_cd = models.CharField(max_length=10, blank=True, null=True)
    presvexecut_cd = models.CharField(max_length=10, blank=True, null=True)
    opertdept_cd = models.CharField(max_length=10, blank=True, null=True)
    chckat_cd = models.CharField(max_length=10, blank=True, null=True)
    nrmltat_cd = models.CharField(max_length=10, blank=True, null=True)
    processdept_cd = models.CharField(max_length=10, blank=True, null=True)
    opertse_cd = models.CharField(max_length=10, blank=True, null=True)
    defectsittn_cd = models.CharField(max_length=10, blank=True, null=True)
    defectcause_cd = models.CharField(max_length=10, blank=True, null=True)
    chck_de = models.CharField(max_length=8, blank=True, null=True)
    opert_cn = models.CharField(max_length=1000, blank=True, null=True)
    opert_user_id = models.CharField(max_length=20, blank=True, null=True)
    begin_dt = models.CharField(max_length=20, blank=True, null=True)
    end_dt = models.CharField(max_length=20, blank=True, null=True)
    cmpnt_sn = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MMS_IMPRMN'


class MmsPresv(models.Model):
    cmpny_id = models.CharField(max_length=20)
    eqp_sn = models.IntegerField()
    presv_sn = models.AutoField(primary_key=True)
    stdrpresv_de = models.CharField(max_length=8, blank=True, null=True)
    presvpd_day = models.CharField(max_length=10, blank=True, null=True)
    cmpnt_sn = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MMS_PRESV'


class SysCmmncdD(models.Model):
    cmpny_id = models.CharField(max_length=20)
    mcode_id = models.CharField(max_length=10)
    dcode_sn = models.AutoField(primary_key=True)
    dcode_nm = models.CharField(max_length=50, blank=True, null=True)
    dcode_val1 = models.CharField(max_length=100, blank=True, null=True)
    dcode_val2 = models.CharField(max_length=100, blank=True, null=True)
    dcode_val3 = models.CharField(max_length=100, blank=True, null=True)
    ord_seq = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SYS_CMMNCD_D'


class SysCmmncdM(models.Model):
    mcode_id = models.CharField(primary_key=True, max_length=10)
    mcode_cd = models.CharField(max_length=20, blank=True, null=True)
    mcode_nm = models.CharField(max_length=50, blank=True, null=True)
    auth_cd = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SYS_CMMNCD_M'


class SysMngr(models.Model):
    mngr_id = models.CharField(primary_key=True, max_length=20)
    mngr_nm = models.CharField(max_length=50, blank=True, null=True)
    auth_cd = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SYS_MNGR'


class UsrCmpny(models.Model):
    cmpny_id = models.CharField(primary_key=True, max_length=20)
    cmpny_nm = models.CharField(max_length=100, blank=True, null=True)
    cmpny_tlphon = models.CharField(max_length=20, blank=True, null=True)
    cmpny_adres1 = models.CharField(max_length=200, blank=True, null=True)
    charger_nm = models.CharField(max_length=20, blank=True, null=True)
    charge_moblphon = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'USR_CMPNY'


class UsrUser(models.Model):
    cmpny_id = models.CharField(primary_key=True, max_length=20)
    user_id = models.CharField(max_length=20)
    user_nm = models.CharField(max_length=20, blank=True, null=True)
    user_pw = models.CharField(max_length=20, blank=True, null=True)
    dept_cd = models.CharField(max_length=10, blank=True, null=True)
    clsf_cd = models.CharField(max_length=10, blank=True, null=True)
    auth_cd = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'USR_USER'
        unique_together = (('cmpny_id', 'user_id'),)


class UtlCldr(models.Model):
    cmpny_id = models.CharField(primary_key=True, max_length=20)
    cldr_de = models.CharField(max_length=8)
    cldrse_cd = models.CharField(max_length=10, blank=True, null=True)
    cldr_cn = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UTL_CLDR'
        unique_together = (('cmpny_id', 'cldr_de'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TblCodeD(models.Model):
    mcode_id = models.CharField(max_length=20)
    code_id = models.CharField(max_length=20)
    code_nm = models.CharField(max_length=200)
    remark = models.CharField(max_length=500, blank=True, null=True)
    code_val1 = models.CharField(max_length=20, blank=True, null=True)
    code_val2 = models.CharField(max_length=20, blank=True, null=True)
    code_val3 = models.CharField(max_length=20, blank=True, null=True)
    use_flag = models.CharField(max_length=1)
    c_date = models.CharField(max_length=20, blank=True, null=True)
    c_userid = models.CharField(max_length=20, blank=True, null=True)
    u_date = models.CharField(max_length=20, blank=True, null=True)
    u_userid = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_code_d'


class TblCodeM(models.Model):
    com_id = models.CharField(max_length=20)
    code_id = models.CharField(primary_key=True, max_length=20)
    code_nm = models.CharField(max_length=200)
    remark = models.CharField(max_length=500, blank=True, null=True)
    code_val1 = models.CharField(max_length=20, blank=True, null=True)
    code_val2 = models.CharField(max_length=20, blank=True, null=True)
    code_val3 = models.CharField(max_length=20, blank=True, null=True)
    use_flag = models.CharField(max_length=1)
    c_date = models.CharField(max_length=20, blank=True, null=True)
    c_userid = models.CharField(max_length=20, blank=True, null=True)
    u_date = models.CharField(max_length=20, blank=True, null=True)
    u_userid = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_code_m'


class Test(models.Model):
    test_pk = models.AutoField(primary_key=True)
    test_col1 = models.CharField(max_length=50, blank=True, null=True)
    test_col2 = models.CharField(max_length=50, blank=True, null=True)
    test_col3 = models.CharField(max_length=50, blank=True, null=True)
    test_col4 = models.CharField(max_length=50, blank=True, null=True)
    test_col5 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'
