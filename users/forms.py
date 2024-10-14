from django import forms


class SignupForm(forms.Form):
	login = forms.CharField(
		max_length=100,
		required=True,
		widget=forms.TextInput(attrs={
			'placeholder': 'Mobile number or email'
		})
	)
	password = forms.CharField(
		max_length=128,
		required=True,
		widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
	)

	full_name = forms.CharField(
		max_length=30,
		required=True,
		widget=forms.TextInput(attrs={'placeholder': 'Full Name'})
	)

	username = forms.CharField(
		max_length=150,
		required=True,
		widget=forms.TextInput(attrs={'placeholder': 'Username'})
	)
