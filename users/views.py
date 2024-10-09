from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import SignupForm
from .service import email_or_phone_number


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
			login(request, user)
			return HttpResponse("Successfully login")
		else:
			return HttpResponse("login or password error")

	return render(request, "index.html")


def signup_page(request):
	if request.method == "POST":
		form = SignupForm(data=request.POST)
		if form.is_valid():
			login_type = email_or_phone_number(form.cleaned_data.get('login'))
			if login_type:
				temp_user = {"user_login": form.cleaned_data.get("login"),
				             "password": form.cleaned_data.get("password"),
				             "full_name": form.cleaned_data.get("full_name"),
				             "username": form.cleaned_data.get("username"),
				             "login_type": login_type}
				request.session["temp_user"] = temp_user
			else:
				return HttpResponse("invalid login")
			return redirect('birthday')

	else:
		form = SignupForm()
		return render(request, "signup.html", {"form": form})


def birthday_page(request):
	if request.method == "POST":
		temp_user = request.session['temp_user']
		login_type = temp_user.get('login_type')
		user_login = temp_user.get('user_login')
		temp_user['date_of_birth'] = request.POST.get('birthday')
		if login_type == "EMAIL":
			return render(request, 'email.html')
		else:
			return render(request, 'phone.html')

	return render(request, "birthday.html")
