from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import SignupForm
from .models import User, EMAIL, PHONE_NUMBER
from .service import email_or_phone_number, send_email
from .models import UserConfirmation


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
			return HttpResponse("Successfully logged in")
		else:
			return HttpResponse("Login or password error")

	return render(request, "index.html")


def signup_page(request):
	if request.method == "POST":
		form = SignupForm(data=request.POST)
		if form.is_valid():
			user_login = email_or_phone_number(form.cleaned_data.get('login'))
			if user_login:

				try:
					temp_user = User.objects.create_user(
						email=form.cleaned_data.get("login") if user_login == EMAIL else None,
						phone_number=form.cleaned_data.get("login") if user_login == PHONE_NUMBER else None,
						password=form.cleaned_data.get("password"),
						first_name=form.cleaned_data.get("full_name"),
						username=form.cleaned_data.get("username"),
						auth_type=user_login,
						is_active=False
					)

					request.session['temp_user_id'] = f"{temp_user.id}"

				except Exception as e:
					return HttpResponse(f"Error: {str(e)}")

				return redirect('birthday')

			return HttpResponse("Invalid user_login type")

	else:
		form = SignupForm()

	return render(request, "signup.html", {"form": form})


def birthday_page(request):
	temp_user_id = request.session.get('temp_user_id')

	if not temp_user_id:
		return HttpResponse("No user found in session!")

	if request.method == "POST":
		date_of_birth = request.POST.get("birthday")
		temp_user = User.objects.get(id=temp_user_id)

		temp_user.date_of_birth = date_of_birth
		temp_user.save()

		verification_code = temp_user.create_verify_code(PHONE_NUMBER if temp_user.phone_number else EMAIL)

		if temp_user.phone_number:
			# send_sms(temp_user.phone_number, verification_code)
			# return render(request,"phone.html")
			pass
		elif temp_user.email:
			send_email(temp_user.email, verification_code)
			return render(request, "email.html")

	return render(request, 'birthday.html')


def confirmation_code_view(request):
	if request.method == "POST":
		temp_user_id = request.session.get('temp_user_id')

		if not temp_user_id:
			return HttpResponse("No user found in session!")

		confirmation_code = request.POST.get("code")

		user_confirmation = UserConfirmation.objects.filter(
			Q(user_id=temp_user_id) & Q(code=confirmation_code) & Q(is_confirmed=False)).last()
		if user_confirmation is None:
			return HttpResponse("invalid code")

		if timezone.now() <= user_confirmation.expire_time:
			user = user_confirmation.user
			user.is_active = True
			user.save()
			user_confirmation.is_confirmed = True
			user_confirmation.save()
			return render(request, "home.html")

		return HttpResponse("Code expired")
