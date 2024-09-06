from django.forms import forms
# from .models import Tekshiruvchi



class Checker(forms.BaseForm):
    class Meta:
        # model = Tekshiruvchi
        fields = ['code']
