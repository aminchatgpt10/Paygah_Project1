from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.


def signup_page(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tour:homepage')

    form = UserCreationForm()
    context = {
        "form": form
    }
    return render(request, 'accounts/signup.html', context)


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')

    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {"form": form})


def logout_page(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")

# def login_page(request):
#     if request.method == "POST":
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect("/")
#
#     form = AuthenticationForm()
#     return render(request, 'accounts/login.html')
#
# # def logout_page(request):
# #     if request.method == "POST":
# #         logout(request.user)
# #         return redirect('/')
