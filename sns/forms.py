from django import forms
from django.contrib.auth.models import User
from .models import Post
from django.core.validators import ValidationError

class LoginForm(forms.Form):
    name = forms.CharField(max_length=30)
    pw = forms.CharField(max_length=30, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, help_text=None)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput, label="Repeat password")
    email = forms.EmailField(max_length=40)

    def clean(self):
        if self.data['password'] != self.data['password2']:
            raise ValidationError("The passwords you typed do not mach. Try again.")
        else:
            return super().clean()

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body', 'image')
        widgets = {'body': forms.TextInput(attrs={'placeholder': "What's up?"}), }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        help_texts = {'username': None}

class ChangePassword(forms.Form):
    pw1 = forms.CharField(widget=forms.PasswordInput, label="Password 1")
    pw2 = forms.CharField(widget=forms.PasswordInput,
                          help_text="Repeat the password",
                          label="Password 2")

    def clean(self):
        if self.data['pw1'] != self.data['pw2']:
            raise ValidationError("The passwords you typed do not match. Try again.")
        else:
            return super().clean()

class CommentForm(forms.Form):
    text = forms.Textarea()
    aka = forms.IntegerField(max_value=10)

