from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/accounts/login/')
    context = {"form": form}
    return render(request, 'accounts/register.html', context)

def login_view(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # # print(username, password)
        # user = authenticate(request, username=username, password=password)
        # if user is None:
        #     context = {"error": "Invalid username or password!"}
        #     return render(request, "accounts/login.html", context=context)
        # login(request, user)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
        return redirect('/')
    else:
        form = AuthenticationForm(request)
        context = {
            "form" : form
        }
    return render(request, "accounts/login.html", context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/accounts/login/')
    return render(request, "accounts/logout.html", {})
