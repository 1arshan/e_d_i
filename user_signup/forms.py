from django import forms


class UserForm(forms.ModelForm):
    password =forms.CharField(widget =forms.PasswordInput)
    confirm_password =forms.CharField(widget =forms.PasswordInput)
    class Meta:
        model =User
        fields =['username','email' ,'password']
