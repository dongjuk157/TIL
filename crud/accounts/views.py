from accounts.forms import CustomUserChangeFrom, CustomUserCreationFrom
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, get_user, update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.views.decorators.http import require_POST, require_safe, require_http_methods

# Create your views here.
@require_safe
def index(request):
    if request.user.is_superuser:
        users = get_user_model().objects.all()
        context = {
            'users': users,
        }
        return render(request, 'accounts/index.html', context)
    else:
        return redirect('articles:index')

@require_http_methods(['GET','POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context ={
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')

@require_http_methods(['GET','POST'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationFrom(request.POST)
        if form.is_valid():
            new_user = form.save()
            auth_login(request, new_user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationFrom()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@login_required
@require_http_methods(['GET','POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeFrom(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:update') 
            # 이부분은 나중에 알람으로 수정되었습니다. 표시를 해줘야할듯
    else:
        form = CustomUserChangeFrom(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

@require_POST
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')

@login_required
@require_http_methods(['GET','POST'])
def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:update')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
    