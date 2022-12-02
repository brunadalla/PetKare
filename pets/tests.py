from pets.models import Pet
from django.test import TestCase


class PetModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.pet_data = {
            "name": "Minerva",
            "age": 6,
            "weight": 30.0,
            "sex": "Female",
            "group": {"scientific_name": "canis familiaris"},
            "traits": [{"name": "clever"}, {"name": "friendly"}, {"name": "playfull"}],
        }

        cls.pet = Pet.objects.create(**cls.actor_data)

    def test_name_max_length(self):
        max_length = self.pet._meta.get_field("name").max_length

        self.assertEqual(max_length, 50)

    def test_sex_max_length(self):
        max_length = self.pet._meta.get_field("sex").max_length

        self.assertEqual(max_length, 20)

    def test_get_traits_count(self):
        result = self.pet.traits_count
        expected = len(self.pet_data['traits'])

        self.assertEqual(result, expected)

    def test_pet_fields(self):
        self.assertEqual(self.pet.name, self.pet_data["name"])
        self.assertEqual(self.pet.age, self.pet_data["age"])
        self.assertEqual(self.pet.weight, self.pet_data["weight"])
        self.assertEqual(self.pet.sex, self.pet_data["sex"])
        
