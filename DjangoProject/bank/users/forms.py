from users.models import CustomUser
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.forms import PasswordInput


class UserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'birthdate']
        widgets = {'password': PasswordInput}

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 4:
            raise ValidationError('too short username', code='short_username')
        if 'a' not in username:
            raise ValidationError('a not in username', code='a_un_error')
        return self.cleaned_data['username']

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if 'a' in first_name:
            raise ValidationError('a in first_name', code='a_fn_error')
        return self.cleaned_data['first_name']

