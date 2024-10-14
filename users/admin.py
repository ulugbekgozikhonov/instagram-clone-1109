from django.contrib import admin

from users.models import User, UserConfirmation


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ["id", "username", "is_staff"]


@admin.register(UserConfirmation)
class UserConfirmationAdmin(admin.ModelAdmin):
	list_display = ["id", "code", "user"]
