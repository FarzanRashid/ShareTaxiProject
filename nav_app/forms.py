from django import forms
from .models import GetUserInfo


class GetUserInfoForm(forms.ModelForm):
    class Meta:
        model = GetUserInfo
        fields = ['location', 'departure_time']