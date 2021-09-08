
from django.contrib.auth.models import User
from django import forms 
from index.models import Atik

from django.core.exceptions import  ValidationError


class AtikNouvoForm(forms.ModelForm):
    class Meta:
        model = Atik
        fields = ('tit', 'jounalis', 'kontni') # lis chan kap genyn nan html lan


    def clean(self):
    
        # mwen rele clean data nan klas paran an
        # pou premier etwayaj pa defo yo

        cleaned_data = super().clean()

        tit = cleaned_data.get("tit")
        jounalis = cleaned_data.get("jounalis")
        kontni = cleaned_data.get("kontni")

        if "med" in kontni:
            raise ValidationError("ou pa dwe mete mo sa nan konti an tanpri")

        if 'jovenel' in jounalis:
            raise ValidationError("ou pa dwe mete nom defen an kom non jounalis mesi")
        
        if 'ayiti pap chanje' in tit:
            raise ValidationError("poukisa ou vle modi pwop peyi tanpri pa ekri sa nan blog mwen an")

        return  cleaned_data

class UserForm(forms.ModelForm):


    class Meta:
        model = User
        fields = ('username', 'password')

        widgets = {
         'password': forms.PasswordInput(attrs={'class': 'input'})
      }
