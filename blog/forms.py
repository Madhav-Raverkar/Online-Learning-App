from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

class ContactForm(forms.Form):
	uname = forms.CharField(label='Name',max_length=100)
	email = forms.CharField(label='Email',max_length=100)
	mobno = forms.IntegerField(label='Mobile Number')
	udisc = forms.CharField(label='Description',max_length=1000)

class UpdateBlogForm(forms.Form):
	title = forms.CharField(label='Title',max_length=100)
	discription = forms.CharField(label='Blog',max_length=1000,widget=forms.Textarea)
	regdate = forms.DateField(label='date')

	def clean_discription(self):

		discription = self.cleaned_data.get('discription')

		if len(discription) < 20:
			raise forms.ValidationError("Blog should contain minimum of 20 Charecters")


		return discription

class CreateBlogForm(forms.Form):
	title = forms.CharField(label='Title',max_length=100)
	discription = forms.CharField(label='Blog',max_length=1000,widget=forms.Textarea)
	regdate = forms.DateField(label='date')

	def clean_discription(self):

		discription = self.cleaned_data.get('discription')

		if len(discription) < 20:
			raise forms.ValidationError("Blog should contain minimum of 20 Charecters")


		return discription

class SignupForm(forms.Form):
	first_name = forms.CharField(label='First Name',max_length=100)
	last_name = forms.CharField(label='Last Name',max_length=100)
	username = forms.CharField(label='UserName',max_length=100)
	email = forms.CharField(label='Email Add',max_length=100)
	password1 = forms.CharField(label='Password',max_length=16,widget = forms.PasswordInput)
	password2 = forms.CharField(label='Confirm Password',max_length=16,widget = forms.PasswordInput)

	def clean(self):	

		password1 = self.cleaned_data['password1']
		password2 = self.cleaned_data['password2']

		if password1 != password2:
			raise forms.ValidationError('Password not Matching ')

		Sym = ['#', '$', '@', '&']

		if len(password1) < 6 :
			raise forms.ValidationError('The length of password should be at least 6')
		if len(password1) > 12 :
			raise forms.ValidationError('The length of password should not be grater than 12')
		if not any(char.isdigit() for char in password1) :
			raise forms.ValidationError('The password should contain at least a number')
		if not any(char.isupper() for char in password1) :
			raise forms.ValidationError('The  password should contain at least Capital')
		if not any(char.islower() for char in password1) :
			raise forms.ValidationError('The password should contain at least Lower')
		if not any(char in Sym for char in password1) :
			raise forms.ValidationError('The  password should be at least a symbol')
		
		return password1


	def clean_username(self):

		username = self.cleaned_data['username']
		if User.objects.filter(username=username):
			raise forms.ValidationError('Username already taken!')
		return username

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email):
			raise forms.ValidationError('Email Taken')
		return email

class LoginForm(forms.Form):
	username = forms.CharField(label='UserName',max_length=100)
	password = forms.CharField(label='Password',max_length=16,widget = forms.PasswordInput)

	def clean(self):

		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		if not User.objects.filter(username=username):
			raise forms.ValidationError("No such username!")

		else:
			user = User.objects.get(username=username)

			if not check_password(password, user.password):
				raise forms.ValidationError('Password is not correct')
