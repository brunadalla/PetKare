from rest_framework.views import APIView, Response, Request, status
from django.shortcuts import get_object_or_404
from .serializers import PetSerializer
from .models import Pet


class PetView(APIView):
    def post(self, request: Request) -> Response:
        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)

        return Response(serializer.data)


class PetDetailView(APIView):
    def get(self, request: Request, pet_id) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)
        serializer = PetSerializer(pet)

        return Response(serializer.data)

    def patch(self, request: Request, pet_id) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)

        serializer = PetSerializer(pet, data=request.data, partial=True)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
    
    def delete(self, request: Request, pet_id) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)
        pet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

