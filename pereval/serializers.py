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

        user_email = user_data.get('email')
        if Users.objects.filter(email=user_email).exists():
            user = Users.objects.get(email=user_email)

        else:
            user = Users.objects.create(**user_data)

        level = Level.objects.create(**level_data)
        coords = Coords.objects.create(**coords_data)

        instance = Added.objects.create(user=user, level=level,
                                        coords=coords, **validated_data)
        instance.save()

        for image_data in images_data:
            Images.objects.create(added=instance, **image_data)
        return instance

    def update(self, instance, validated_data):
        if instance.status == 'New':
            if 'user' in validated_data:
                raise serializers.ValidationError('Update error. User fields are not changeable')

            if 'level' in validated_data:
                level = self.fields['level']
                level_instance = instance.level
                level_data = validated_data.pop('level')
                level.update(level_instance, level_data)

            if 'coords' in validated_data:
                coords = self.fields['coords']
                coors_instance = instance.coords
                coords_data = validated_data.pop('coords')
                coords.update(level_instance, coords_data)

            if 'images' in validated_data:
                images_data = validated_data.pop('images')

                for image in images_data:
                    image_id = image.get('id', None)
                    if image_id:
                        inv_image = Images.objects.get(id=image_id)
                        inv_image.data = image.get('data', inv_image.data)
                        inv_image.title = image.get('title', inv_image.title)
                        inv_image.save()
                    else:
                        Images.objects.create(added=instance, **image)

                images_dict = dict((i.id, i) for i in instance.images.all())
                if len(images_data) == 0:
                    for image in images_dict.values():
                        image.delete()

            return super(AddedSerializer, self).update(instance, validated_data)
            raise serializers.ValidationError('Update error. Object status is not `New`')
