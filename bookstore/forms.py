from django import forms
from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = UserBook
        exclude =['author','review_stars','bookcover','bookfile']
        widgets = {
            "genre": forms.Select(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"placeholder": "Book Title", "class": "form-control"}),
            "type": forms.Select(attrs={"class": "form-control"}),
            "review": forms.Textarea(attrs={"placeholder": "Review", "class": "form-control"}),
            "favorite": forms.CheckboxInput(attrs={"class": "form-control","style":"max-width:30px;float:left"}),

        }