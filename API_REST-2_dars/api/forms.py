from django.forms import ModelForm
from .models import Employee


class CreateForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name', 'position', 'position', 'info',]
