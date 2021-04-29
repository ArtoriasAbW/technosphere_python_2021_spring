from departments.models import Department
from django.core.exceptions import ValidationError
from django.forms import ModelForm


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'address', 'phone_number']

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        for character in phone_number:
            if character.isalpha():
                raise ValidationError('Номер телефона не должен содержать букв', code='alpha_in_pn')
        return self.cleaned_data['phone_number']

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name[0].isalpha():
            raise ValidationError('Названия отделения должно начинаться с буквы', code='letter_first')
        if name[0].capitalize() != name[0]:
            raise ValidationError('Название отделения должно начинаться с ЗАГЛАВНОЙ буквы', code='upper_first')
        return self.cleaned_data['name']
