from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout, authenticate

from .form import LoginForm

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            cmpny_id = login_form.cleaned_data['cmpny_id']
            user_id = login_form.cleaned_data['user_id']
            user_pw = login_form.cleaned_data['user_pw']

            user = authenticate(
                user_id=user_id,
                user_pw=user_pw
            )
            # 인증 성공
            if user:
                django_login(request, user)
                return redirect('dtm:index')
            # 인증 실패
            login_form.add_error(None, '아이디 또는 비밀번호가 올바르지 않습니다')
    else:
        login_form = LoginForm()
        context = {
            'login_form': login_form,
        }
    return render(request, 'dtm_user/login.html', context)

def logout(request):
    django_logout(request)
    return redirect('post:post_list')