from django.db import models
from django.urls import reverse


class Animal(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()  
    description = models.TextField()  
    medical_history = models.TextField()  
    care_needs = models.TextField()  
    photo = models.ImageField(upload_to='animals/', blank=True)  
    shelter = models.ForeignKey('Shelter', on_delete=models.CASCADE, related_name='animals')
    available_for_adoption = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('view-animal', kwargs={'pk': self.pk})

class AdoptionRequest(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    adopter = models.CharField(max_length=100)
    adopter_address = models.TextField(default='')
    status_choices = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending')
    request_date = models.DateTimeField()
    approval_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.adopter} - {self.animal.name} - {self.status}"

class Shelter(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    description = models.TextField()  
    is_verified = models.BooleanField(default=True)  

    def __str__(self):
        return self.name

class Donation(models.Model):
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE, related_name='donations')
    donor_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donation_date = models.DateTimeField(auto_now_add=True)
    anonymous = models.BooleanField(default=False)

    def __str__(self):
        return f"Donation from {self.donor_name} to {self.shelter.name} of ${self.amount}"
