from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Amenity
from .serializers import AmenitySerializer


# Create your views here.
class Amenities(APIView):

    def get(self, request):
        amenities = Amenity.objects.all()
        serializer = AmenitySerializer(amenities, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            amenity = serializer.save()
            return Response(AmenitySerializer(amenity).data)
        else:
            return Response(serializer.errors)


class AmenityDetail(APIView):

    def get(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
