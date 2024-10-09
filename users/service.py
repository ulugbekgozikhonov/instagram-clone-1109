import re

EMAIL_REGEX = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
PHONE_NUMBER_REGEX = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'


def email_or_phone_number(user_inp):
	if re.fullmatch(EMAIL_REGEX, user_inp):
		return "EMAIL"
	elif re.fullmatch(PHONE_NUMBER_REGEX, user_inp):
		return "PHONE_NUMBER"
	else:
		return False
