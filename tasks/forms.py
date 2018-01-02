#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from tasks.models import *


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', "task_type", "task_desc", 'task_applyer_name', 'task_approve_name']
        widgets = {
            'task_name': forms.TextInput(attrs={'class': 'form-control'}),
            'task_type': forms.TextInput(attrs={'class': 'form-control'}),
            'task_desc': forms.TextInput(attrs={'class': 'form-control'}),
            'task_applyer_name': forms.TextInput(attrs={'class': 'form-control'}),
<<<<<<< HEAD
            'task_approve_name': forms.TextInput(attrs={'class': 'form-control'})
        }


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file', )


class FileUploadForm(forms.Form):
    my_file = forms.FileField()
=======
            'task_approve_name': forms.TextInput(attrs={'class': 'form-control'}),
            'tool_script': forms.Textarea(

            ),
        }
>>>>>>> 863605f36a804274c50df5f9d59dee8195cd690f
