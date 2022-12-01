from rest_framework import serializers
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer

from .models import Pet, PetSex
from groups.models import Group
from traits.models import Trait

class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=PetSex.choices,
        default=PetSex.NOT_INFORMED,
    )

    group = GroupSerializer()
    traits = TraitSerializer(many=True)

    traits_count = serializers.SerializerMethodField()

    def get_traits_count(self, obj):
        return len(obj.traits.all())

    def create(self, validated_data: dict):
        group_request = validated_data.pop("group")
        traits_request = validated_data.pop("traits")

        created_group, _ = Group.objects.get_or_create(**group_request)

        created_obj = Pet.objects.create(**validated_data, group=created_group)

        for trait in traits_request:
            created_trait, _ = Trait.objects.get_or_create(**trait)
            created_obj.traits.add(created_trait)

        return created_obj

    def update(self, instance: Pet, validated_data: dict):
        for key, value in validated_data.items():
            if key == "group":
                created_group, _ = Group.objects.get_or_create(**value)
                instance.group.set(created_group, clear=True)

            elif key == "traits":
                traits = list()

                for trait in value:
                    created_trait, _ = Trait.objects.get_or_create(**trait)
                    traits.append(created_trait)

                instance.traits.set(traits, clear=True)

            else:
                setattr(instance, key, value)

        instance.save()

        return instance
