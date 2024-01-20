from django import forms 
from category.models import catagory_model

class category_form(forms.ModelForm):
    class Meta:
        model = catagory_model
        fields = '__all__'
