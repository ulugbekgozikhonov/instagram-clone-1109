from django.contrib.auth.models import AbstractUser
from django.db import models

import uuid


class GenderType(models.TextChoices):
	MALE = "MALE", "Male"
	FEMALE = "FEMALE", "Female"
	UNKNOWN = "UNKNOWN", "Unknown"


class User(AbstractUser):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	phone_number = models.CharField(max_length=31, null=True, blank=True, unique=True)
	date_of_birth = models.DateField(null=True, blank=True)
	avatar = models.ImageField(upload_to="users/avatars/", null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	gender = models.CharField(max_length=7, choices=GenderType.choices, default=GenderType.UNKNOWN)
