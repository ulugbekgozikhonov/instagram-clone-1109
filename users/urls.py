from django.urls import path
from .views import login_page, signup_page, birthday_page

urlpatterns = [
	path("", login_page, name='login'),
	path("signup/", signup_page, name='signup'),
	path("birthday/", birthday_page, name="birthday")

]
