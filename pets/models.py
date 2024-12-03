from django.db import models
from django.utils import timezone
    
class Customer(models.Model):
    email = models.EmailField()
    name = models.CharField(
        null=True, 
        max_length=255)
    phone_number = models.CharField(null=True, max_length=15)
    paided_customer = models.BooleanField(default=False)
    validated = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def class_name(self):
        return self.__class__.__name__
    
    class Meta:
        ordering = ['name']
    
class AnimalType(models.Model):
    name = models.CharField(max_length=255)
    
class Breed(models.Model):
    name = models.CharField(max_length=255)
    
    animal_type = models.ForeignKey(
        AnimalType,
        on_delete=models.PROTECT
    )
    
class Animal(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    birt_date = models.DateField(null=True)
    memorial_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    owner = models.ForeignKey(
        Customer, 
        null=True,
        blank=True,
        on_delete=models.CASCADE)
    
    animal_type = models.ForeignKey(
        AnimalType,
        default=1,
        on_delete=models.PROTECT
    )
    
    animal_breed = models.ForeignKey(
        Breed,
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )

class Guardian(models.Model):
    STATUS_ACTIVE = 'A'
    STATUS_INACTIVE = 'I'
    
    STATUS = [
        (STATUS_ACTIVE, 'Active'),
        (STATUS_INACTIVE, 'Inactive')
    ]
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pets = models.ManyToManyField(Animal)
    status = models.CharField(
        max_length=1, 
        choices=STATUS, 
        default=STATUS_ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Allergy(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']
    
class AnimalAllergy(models.Model):
    ALLERGY_LOW = 'L'
    ALLERGY_MEDIUM = 'M'
    ALLERGY_HIGH = 'H'
    ALLERGY_SEVERE = 'S'
    ALLERGY_DEADLY = 'D'
    
    ALLERGY_LEVEL = [
        (ALLERGY_LOW, 'Low'),
        (ALLERGY_MEDIUM, 'Medium'),
        (ALLERGY_HIGH, 'High'),
        (ALLERGY_SEVERE, 'Severe'),
        (ALLERGY_DEADLY, 'Deadly'),
    ]
    
    allergy_level = models.CharField(max_length=1, choices=ALLERGY_LEVEL, default=ALLERGY_MEDIUM) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE
    )
    
    allergy = models.ForeignKey(
        Allergy,
        on_delete=models.CASCADE
    )
    
class VeterinaryAppoitment(models.Model):
    VET_REASON_CHECKUP = 'C'
    VET_REASON_VACCINE = 'V'
    VET_REASON_INJURY = 'I'
    VET_REASON_DIGESTIVE = 'D'
    VET_REASON_SKIN = 'S'
    VET_REASON_DENTAL = 'E'
    VET_REASON_BEHAVIOR = 'B'
    VET_REASON_PARASITE = 'P'
    VET_REASON_REPRODUCTION = 'R'
    VET_REASON_OTHER = 'O'
    
    VET_REASON = [
        (VET_REASON_CHECKUP, 'Checkup'),
        (VET_REASON_VACCINE, 'Vaccine'),
        (VET_REASON_INJURY, 'Injury'),
        (VET_REASON_DIGESTIVE, 'Digestive'),
        (VET_REASON_SKIN, 'Skin'),
        (VET_REASON_DENTAL, 'Dental'),
        (VET_REASON_BEHAVIOR, 'Behavior'),
        (VET_REASON_PARASITE, 'Parasite'),
        (VET_REASON_REPRODUCTION, 'Reproduction'),
        (VET_REASON_OTHER, 'Other'),
    ]
    
    date = models.DateField(null=False, blank=False, default=timezone.now)
    veterinarian = models.CharField(max_length=255)
    notes = models.TextField()
    reason = models.CharField(
        max_length=1, 
        choices=VET_REASON, 
        default=VET_REASON_CHECKUP
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    animal = models.ForeignKey(
        Animal,
        on_delete=models.PROTECT
    )
    
class AppoitmentLog(models.Model):
    log = models.TextField(),
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class AppoitmentMedication(models.Model):
    medication = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    appoitment = models.ForeignKey(
        VeterinaryAppoitment,
        on_delete=models.CASCADE
    )
    