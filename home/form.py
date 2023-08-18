from django import forms

from .models import contactforms

# creating a form
class LoginForm(forms.Form):
    user_name = forms.CharField(label='', max_length = 100, widget=forms.TextInput(attrs={'class':'box', 'placeholder' : 'User name'}))
    password = forms.CharField(label='', widget = forms.PasswordInput(attrs={'class':'box', 'placeholder' : 'Password'}))

class RegisterForm(forms.Form):
    user_name = forms.CharField(label='', max_length = 100, widget=forms.TextInput(attrs={'class':'box', 'placeholder' : 'User name'}))
    password = forms.CharField(label='', widget = forms.PasswordInput(attrs={'class':'box', 'placeholder' : 'Password'}))
    email = forms.CharField(label='', max_length = 100, widget=forms.TextInput(attrs={'class':'box', 'placeholder' : 'Email'}))
    c_password = forms.CharField(label='', widget = forms.PasswordInput(attrs={'class':'box', 'placeholder' : 'Confirm Password'}))

    
class form_contact(forms.ModelForm):
    fullname = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'box', 'placeholder' : 'Your name'}))
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'box', 'placeholder' : 'Email'}))
    phone = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'box', 'placeholder' : 'Phone'}))
    message = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'box box-message', 'placeholder' : 'Message'}))

    class Meta:
        model = contactforms
        fields = ['fullname', 'email', 'phone', 'message']