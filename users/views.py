from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignupForm
from .models import User
from django.db.models import Q


# def login_page(request):
# 	if request.method == "POST":
# 		user_login = request.POST.get("login")
# 		password = request.POST.get("password")
# 		user = User.objects.filter(Q(username=user_login) | Q(phone_number=user_login) | Q(email=user_login)).first()
# 		if user is not None:
# 			if user.check_password(password):
# 				login(request, user)
# 				return HttpResponse("Successfully login")
# 			else:
# 				return HttpResponse("username or password error")
# 		else:
# 			return HttpResponse("login or password error")
#
# 	return render(request, "index.html")

def login_page(request):
	if request.method == "POST":
		user_inp = request.POST.get("user_inp")
		password = request.POST.get("password")
		user = authenticate(request, username=user_inp, password=password)
		if user is not None:
			return HttpResponse("Successfully login")
		else:
			return HttpResponse("login or password error")

	return render(request, "index.html")


def signup_page(request):
	if request.method == "POST":
		print("keldi")
		form = SignupForm(data=request.POST)
		if form.is_valid():
			temp_user = {"user_login": form.cleaned_data.get("login"), "password": form.cleaned_data.get("password"),
			             "full_name": form.cleaned_data.get("full_name"),
			             "username": form.cleaned_data.get("username")}
			request.session["temp_user"] = temp_user
			print(request.session.get("temp_user"), "temp_user")
			return redirect('birthday')

	else:
		form = SignupForm()
		return render(request, "signup.html", {"form": form})


def birthday_page(request):
	return render(request, "birthday.html")
