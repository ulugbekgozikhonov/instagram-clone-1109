import re
import random

from django.core.mail import send_mail
from django.conf import settings

from users.models import EMAIL, PHONE_NUMBER

EMAIL_REGEX = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
PHONE_NUMBER_REGEX = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'


def email_or_phone_number(user_inp):
	if re.fullmatch(EMAIL_REGEX, user_inp):
		return EMAIL
	elif re.fullmatch(PHONE_NUMBER_REGEX, user_inp):
		return PHONE_NUMBER
	else:
		return False


def send_email(to_whom, code):
	send_mail(
		subject="Instagram code",
		message=f"Your verify code>>>: {code}",
		from_email=settings.EMAIL_HOST_USER,
		recipient_list=[to_whom]
	)
