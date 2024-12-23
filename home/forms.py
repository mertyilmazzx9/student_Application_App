

from django import forms
from .models import Basvuru


class BasvuruForm(forms.ModelForm):
    class Meta:
        model = Basvuru
        fields = ['name','surname', 'momname', 'email', 'message' ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "İsim"}),
            'surname': forms.TextInput(attrs={'placeholder': "soyİsim"}),
            'momname': forms.TextInput(attrs={'placeholder': "anne adı"}),
            'email': forms.EmailInput(attrs={'placeholder': "Emailiniz"}),
            'message': forms.Textarea(attrs={'placeholder': "Mesajınız"}),



        }