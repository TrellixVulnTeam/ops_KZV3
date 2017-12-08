#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from users.models import *


class UserGroupModelForm(forms.ModelForm):
    class Meta:
        model = UserGroup
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.TextInput(attrs={'class': 'form-control'})
        }


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ('username', 'password', 'name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username@zofund.com'}),
        }
