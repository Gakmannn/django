from django import forms
 
class UserForm(forms.Form):
  name = forms.CharField(label='NAME', widget=forms.TextInput(attrs={"class":"myfield"}))
  age = forms.IntegerField()
  # passwors = forms.CharField(widget=forms.PasswordInput, min_length=6)