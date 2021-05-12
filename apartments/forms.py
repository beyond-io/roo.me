from django import forms
from .models import Apartment
from django.core.validators import MinValueValidator


class ApartmentDetailsUpdateForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = [
            'date_posted',
            'city',
            'address',
            'rent',
            'num_of_roomates',
            'num_of_rooms',
            'start_date',
            'about',
            'is_relevant',
            'image_url'
            ]


class ApartmentCreationForm(forms.ModelForm):
    rent = forms.IntegerField(validators=[MinValueValidator(limit_value=0)])
    num_of_roomates = forms.IntegerField(validators=[MinValueValidator(limit_value=0)])
    num_of_rooms = forms.IntegerField(validators=[MinValueValidator(limit_value=0)])

    class Meta:
        model = Apartment
        fields = (
            'city',
            'address',
            'rent',
            'num_of_roomates',
            'num_of_rooms',
            'start_date',
            'about',
        )

    def save(self, commit=False):
        if commit:
            raise ValueError("Can't save to the data-base without owner field")
        else:
            new_apartment = super().save()
            return new_apartment
