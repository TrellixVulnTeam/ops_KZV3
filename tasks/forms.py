#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from tasks.models import *


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', "task_type", "task_desc", 'task_applyer_name', 'task_approve_name']
        widgets = {
            'task_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'task_type': forms.TextInput(attrs={'class': 'form-control'}),
            'task_desc': forms.TextInput(attrs={'class': 'form-control'}),
            'task_applyer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'task_approve_name': forms.TextInput(attrs={'class': 'form-control'}),
            'tool_script': forms.Textarea(

            ),
        }