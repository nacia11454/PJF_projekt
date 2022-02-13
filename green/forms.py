from django.forms import ModelForm
from .models import User, Care

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name_us', 'password']

class CareForm(ModelForm):
    class Meta:
        model = Care
        fields = ['plant', 'user', 'care_date']