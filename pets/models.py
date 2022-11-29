from django.db import models

class PetSex(models.TextChoices):
    male = "Male"
    female = "Female"
    not_Informed = "Not Informed"

class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(
        max_length=20,
        choices=PetSex.choices,
        default=PetSex.not_Informed
    )
    
    group = models.ForeignKey(
        "groups.Group", on_delete = models.CASCADE, related_name='pets'
    )