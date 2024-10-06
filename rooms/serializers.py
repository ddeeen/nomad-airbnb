from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = ["name", "description"]


class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "name", "country", "city", "price"]


class RoomDetailSerializer(ModelSerializer):

    owner = TinyUserSerializer()
    amenities = AmenitySerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Room
        fields = "__all__"
