from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from simplemathcaptcha.fields import MathCaptchaField


#forms here
class UserCreationForm(UserCreationForm):
    captcha = MathCaptchaField()
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']

class UserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name','last_name','email')