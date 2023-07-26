from .models import *
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        exclude = ['added']


class AddedSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    level = LevelSerializer()
    coords = CoordsSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = Added
        fields = '__all__'
        read_only_fields = [
            'pk',
            'status',
            'add_time',
        ]

    def create(self, validated_data):
        """Method for creating a new pass with all the information about it."""
        user_data = validated_data.pop('user')
        level_data = validated_data.pop('level')
        coords_data = validated_data.pop('coords')
        images_data = validated_data.pop('images')

        user = Users.objects.create(**user_data)
        level = Level.objects.create(**level_data)
        coords = Coords.objects.create(**coords_data)

        instance = Added.objects.create(user=user, level=level,
                                        coords=coords, **validated_data)
        instance.save()

        for image_data in images_data:
            Images.objects.create(added=instance, **image_data)
        return instance
