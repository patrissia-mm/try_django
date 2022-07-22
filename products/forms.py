from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    tittle=forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your tittle"}))
    description=forms.CharField(required=False, widget=forms.Textarea(attrs={
        "placeholder":"Your description",
        "rows":15,
        "cols":100,
        "id":"id_for_textarea"
    }))
    class Meta:
        model=Product
        fields=[
            'tittle',
            'description',
            'price'
        ]
    def clean_tittle(self,*args,**kargs):
        tittle=self.cleaned_data.get("tittle")
        if not "CFE" in tittle:
            return tittle
        else:
            raise forms.ValidationError("This is not a valid tittle")

class RawProductForm(forms.Form):
    tittle=forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Your title"}))
    description=forms.CharField(required=False, widget=forms.Textarea(attrs={
        "placeholder":"Your Textarea",
        "rows":20,
        "cols":120,
        "class":"new-class-name two",
        "id":"id_for_textarea"

    }))
    price=forms.DecimalField()