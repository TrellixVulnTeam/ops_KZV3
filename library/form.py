from    django import forms
from .models import  librarys
class LibrarysForm(forms.ModelForm):
    class Meta:
        model = librarys
        fields = '__all__'
        labels={
            "file": "上传文件"
        }
        widgets = {
            # 'content': forms.Textarea(
            #     attrs={'id': 'editor','type':"text/plain",}),
        }
        help_texts = {
        }
        error_messages = {
        }





