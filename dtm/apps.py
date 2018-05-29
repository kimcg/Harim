from django.apps import AppConfig
from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class DtmConfig(AppConfig):
    name = 'dtm'
    verbose_name = '관리'

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
    #layout = 'vertical'
    menu = (
        ParentItem('관리', children=[
            ChildItem(model='dtm.syscmmncdm'),
            ChildItem(model='dtm.usrcmpny'),
            ChildItem(model='dtm.usruser'),
        ], icon='fa fa-leaf'),
        ParentItem('인증 및 권한', children=[
            ChildItem('사용자', 'auth.user'),
            ChildItem('사용자 그룹', 'auth.group'),
        ], icon='fa fa-users'),
        ParentItem('관리자', children=[
            ChildItem('비밀번호 변경', url='admin:password_change'),

        ], icon='fa fa-cog'),

    )

    def ready(self):
        super(SuitConfig, self).ready()

        # DO NOT COPY FOLLOWING LINE
        # It is only to prevent updating last_login in DB for demo app
        self.prevent_user_last_login()

    def prevent_user_last_login(self):
        """
        Disconnect last login signal
        """
        from django.contrib.auth import user_logged_in
        from django.contrib.auth.models import update_last_login
        user_logged_in.disconnect(update_last_login)

