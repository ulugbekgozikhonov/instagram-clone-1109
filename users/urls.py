from django.urls import path
from .views import login_page, signup_page, birthday_page, confirmation_code_view

urlpatterns = [
	path("", login_page, name='login'),
	path("signup/", signup_page, name='signup'),
	path("birthday/", birthday_page, name="birthday"),
	path("confirmation-code/", confirmation_code_view, name="confirmation"),

]
