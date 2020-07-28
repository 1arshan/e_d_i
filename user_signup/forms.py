from django import forms


#class UserForm(forms.ModelForm):
class PasswordChangeForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    """class Meta:
        # model = User
        fields = ['password', 'confirm_password']
"""