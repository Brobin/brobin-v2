from django import forms

from .models import BigFish


class FishForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FishForm, self).__init__(*args, **kwargs)
        self.fields['year'].widget.attrs['class'] = 'form-control'
        self.fields['species'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = BigFish
        fields = 'year', 'species', 'length', 'weight'
