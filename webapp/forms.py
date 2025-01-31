from django import forms
from .models import Animal, AdoptionRequest, Shelter
from django.utils import timezone

from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'breed', 'age', 'description', 'medical_history', 'care_needs', 'photo', 'shelter', 'available_for_adoption']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'breed': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'medical_history': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'care_needs': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'shelter': forms.Select(attrs={'class': 'form-control'}),
            'available_for_adoption': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class AdoptionRequestForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = ['animal', 'adopter', 'adopter_address', 'status', 'approval_date']
        widgets = {
            'adopter_address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'animal': forms.Select(attrs={'class': 'form-control'}),
            'adopter': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'approval_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:  
            self.instance.request_date = timezone.now()

class ShelterForm(forms.ModelForm):
    class Meta:
        model = Shelter
        fields = ['name', 'address', 'phone_number', 'email', 'website', 'description', 'is_verified']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'is_verified': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }