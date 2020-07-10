from django.forms import ModelForm
from .models import wishes
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class wishform(ModelForm):
    class Meta:
        model = wishes
        fields = [
            'wish_tittle', 'wish_description', 'wish_status'
        ]


class myuserform(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        ]
