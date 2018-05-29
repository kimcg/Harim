from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class UsrUserManager(BaseUserManager):
    """
    전달된 데이터로 유저를 생성하고 저장합니다.
    """
    def create_user(self, user_id, user_nm, password):
        if not user_id:
            raise ValueError('ID Required!')

        user = self.model(user_id=user_id, user_nm=user_nm, is_active=True)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, username, password):
        """
        전달된 데이터로 관리자를 생성하고 저장합니다.
        처음은 manage.py를 이용해서 만듦(createsuperuser)
        """
        user = self.create_user(user_id, username, password)

        user.is_superuser = True
        user.save(using=self._db)
        return user

class UsrUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(max_length=20, verbose_name='아이디')
    user_nm = models.CharField(max_length=20, blank=True, null=True, verbose_name='이름')
    dept_cd = models.CharField(max_length=10, blank=True, null=True, verbose_name='부서')
    clsf_cd = models.CharField(max_length=10, blank=True, null=True, verbose_name='')
    auth_cd = models.CharField(max_length=10, blank=True, null=True, verbose_name='권한')
    cmpny_id = models.CharField(primary_key=True, max_length=20, verbose_name='회사')
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UsrUserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['cmpny_id', 'user_id']

    class Meta:
        ordering = ('user_id',)
        verbose_name_plural = '사용자'
        verbose_name = '사용자'
        managed = False
        db_table = 'USR_USER'
        unique_together = (('cmpny_id', 'user_id'),)

    def __str__(self):
        return '사용자: {}'.format(self.user_nm)

    def get_short_name(self):
        return self.user_id

    def get_full_name(self):
        return self.user_id

    def get_username(self):
        return self.user_id



