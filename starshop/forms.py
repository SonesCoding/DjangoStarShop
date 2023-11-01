from django import forms
from .models import Star, Quote, cartDetails


class StarForm(forms.ModelForm):
    class Meta:
        model = Star
        fields = '__all__'
        
class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = '__all__'
        
    def clean_slug(self):
        return self.cleaned_data['slug'].lower()
    
class CartForm(forms.ModelForm):
    class Meta:
        model = cartDetails
        fields = '__all__'
        
#class TagForm(forms.Form):
    #name = forms.CharField(max_length=40, help_text='A label for URL')
    
   # def save(self):
           # newTag = Tag.objects.create(
           #  name= self.cleaned_data['name'])
           # return newTag