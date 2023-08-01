from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from pereval.models import Added, Users, Coords, Level, Images
from pereval.serializers import AddedSerializer


class AddedTest(APITestCase):
    def setUp(self):
        self.setup_data = Added.objects.create(
            title="Northern ural",
            user=Users.objects.create(
                first_name="Sonya",
                surname="Ivanovna",
                last_name="Son",
                email="sona@example.com",
                phone="1745622255"
            ),
            level=Level.objects.create(
                autumn="",
                spring="",
                summer="1S",
                winter=""
            ),
            coords=Coords.objects.create(
                latitude=61.7548481,
                longitude=59.4605267,
                height=1096
            )
        )
        self.image_1 = Images.objects.create(
            added=self.setup_data,
            images="https://images.app.goo.gl/US4ATxDTe7ni4aE99",
            title="Start"
        )
        self.image_2 = Images.objects.create(
            added=self.setup_data,
            images="https://images.app.goo.gl/sV5fE3sdCGX9UaYi6",
            title="Finished"
        )

        self.setup_data_status_not_new = Added.objects.create(
            title="Northern ural",
            status='ACC',
            user=Users.objects.create(
                first_name="Tonya",
                surname="Ivanovna",
                last_name="Sons",
                email="Toni@example.com",
                phone="7855999255"
            ),
            level=Level.objects.create(
                winter="",
                summer="",
                autumn="1S",
                spring=""
            ),
            coords=Coords.objects.create(
                latitude=61.7548481,
                longitude=59.4605267,
                height=1096
            )
        )
        self.image_1 = Images.objects.create(
            added=self.setup_data,
            images="https://images.app.goo.gl/US4ATxDTe7ni4aE99",
            title="Start"
        )
        self.image_2 = Images.objects.create(
            added=self.setup_data,
            images="https://images.app.goo.gl/sV5fE3sdCGX9UaYi6",
            title="Finished"
        )

    def test_get(self):
        url = reverse('submitdata-list')
        response = self.client.get(url)
        serializer_data = AddedSerializer([self.setup_data, self.setup_data_status_not_new], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_detail(self):
        url = reverse('submitdata-detail', args=(self.setup_data.id,))
        response = self.client.get(url)
        serializer_data = AddedSerializer(self.setup_data).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.json())

    def test_post_valid(self):
        objects_count_before = Added.objects.count()
        user_count_before = Users.objects.count()
        new_data = {
            "title": "Northern ural",
            "user": {
                "first_name": "Alexander",
                "surname": "Alexandrovich",
                "last_name": "Alexandrov",
                "email": "aaa@googl.com",
                "phone": "359998522"
            },
            "coords": {
                "latitude": 48.456,
                "longitude": 63.776,
                "height": 874
            },
            "level": {
                "summer": "1D"
            },
            "images": []
        }

        url = reverse('submitdata-list')
        response = self.client.post(url, new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(objects_count_before + 1, Added.objects.count())
        self.assertEqual(user_count_before + 1, Users.objects.count())

    def test_post_valid_user_already_exists(self):
        objects_count_before = Added.objects.count()
        user_count_before = Users.objects.count()
        new_data = {
            "title": "Northern ural",
            "user": {
                "first_name": "Ivan",
                "second_name": "Ivanovich",
                "last_name": "Ivanov",
                "email": "ivan@gmail.com",
                "phone": "35555555555"
            },
            "coords": {
                "latitude": 87.4864,
                "longitude": 75.9678,
                "height": 1150
            },
            "level": {
                "winter": "1D"
            },
            "images": [
                {
                    "images": "https://images.app.goo.gl/sV5fE3sdCGX9UaYi6",
                    "title": "Start"
                }
            ]
        }

        url = reverse('submitdata-list')
        response = self.client.post(url, new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(objects_count_before + 0, Added.objects.count())
        self.assertEqual(user_count_before, Users.objects.count())

    def test_post_invalid_user(self):
        objects_count_before = Added.objects.count()
        new_data = {
            "title": "Northern ural",
            "other_title": "Ural",
            "user": {
                "first_name": "Sonya",
                "second_name": "Ivanovna",
                "last_name": "Son",
                "phone": "1745622255"
            },
            "coords": {
                "latitude": 61.7548481,
                "longitude": 59.4605267,
                "height": 1096
            },
            "level": {
                "winter": "",
                "summer": "",
                "autumn": "1S",
                "spring": ""
            },
            "images": [
                {"images": "https://images.app.goo.gl/US4ATxDTe7ni4aE99", "title": "Start"},
                {"images": "https://images.app.goo.gl/sV5fE3sdCGX9UaYi6", "title": "Finished"}]
        }

        url = reverse('submitdata-list')
        response = self.client.post(url, new_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(objects_count_before, Added.objects.count())

    def test_post_invalid_coords(self):
        objects_count_before = Added.objects.count()
        new_data = {
            "title": "Northern ural",
            "other_title": "Ural2",
            "user": {
                "first_name": "Sonya",
                "second_name": "Ivanovna",
                "last_name": "Son",
                "email": "sona@example.com",
                "phone": "1745622255"
            },
            "coords": {
                "height": 1096
            },
            "level": {
                "winter": "",
                "summer": "",
                "autumn": "1S",
                "spring": ""
            },
            "images": [
                {"images": "https://kipmu.ru/wp-content/uploads/mountain.jpg", "title": "Start"},
                {"images": "https://natworld.info/wp-content/uploads/2020/04/gora-fudzi.jpg", "title": "Finished"}
            ]
        }

        url = reverse('submitdata-list')
        response = self.client.post(url, new_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(objects_count_before, Added.objects.count())

    def test_patch_valid_title(self):
        url = reverse('submitdata-detail', args=(self.setup_data.id,))
        new_data = {
            "title": "Sibir"
        }

        response = self.client.patch(url, data=new_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.setup_data.refresh_from_db()
        self.assertEqual('Sibir', self.setup_data.title)

    def test_patch_valid_coords_level(self):
        url = reverse('submitdata-detail', args=(self.setup_data.id,))
        new_data = {
            "coords": {
                "longitude": 59.4605267
            },
            "level": {
                "autumn": "1S"
            }
        }

        response = self.client.patch(url, data=new_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.setup_data.refresh_from_db()
        self.assertEqual('1S', self.setup_data.level.autumn)

    def test_patch_valid_add_image(self):
        url = reverse('submitdata-detail', args=(self.setup_data.id,))
        images_count = Images.objects.filter(added=self.setup_data).count()
        new_data = {
            "images": [
                {
                    "images": "https://images.app.goo.gl/US4ATxDTe7ni4aE99",
                    "title": "through"
                }
            ]
        }

        response = self.client.patch(url, data=new_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.setup_data.refresh_from_db()
        self.assertEqual(images_count + 1, Images.objects.filter(added=self.setup_data).count())

    def test_patch_valid_update_image(self):
        url = reverse('submitdata-detail', args=(self.setup_data.id,))
        image_id = Images.objects.filter(added=self.setup_data).values_list('id', flat=True)[0]
        images_count = Images.objects.filter(added=self.setup_data).count()
        new_data = {
            "images": [
                {
                    "id": image_id,
                    "images": "https://images.app.goo.gl/US4ATxDTe7ni4aE99",
                    "title": "through"
                }
            ]
        }

        response = self.client.patch(url, data=new_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.setup_data.refresh_from_db()
        self.assertEqual(images_count + 1, Images.objects.filter(added=self.setup_data).count())

    def test_patch_valid_clear_image_list(self):
        url = reverse('submitdata-detail', args=(self.setup_data.id,))
        new_data = {
            "images": []
        }

        response = self.client.patch(url, data=new_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.setup_data.refresh_from_db()
        self.assertEqual(0, Images.objects.filter(added=self.setup_data).count())

    def test_patch_invalid_status(self):
        url = reverse('submitdata-detail', args=(self.setup_data_status_not_new.id,))
        new_data = {
            "title": "Sibir"
        }

        response = self.client.patch(url, data=new_data, format='json')
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_patch_invalid_user(self):
        url = reverse('submitdata-detail', args=(self.setup_data.id,))
        new_data = {
            "user": {
                "first_name": "Maya"
            }
        }

        response = self.client.patch(url, data=new_data, format='json')
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_patch_invalid_level_coords(self):
        url = reverse('submitdata-detail', args=(self.setup_data.id,))
        new_data = {
            "level": {
                "summer": "Maya"
            },
            "coords": {}
        }

        response = self.client.patch(url, data=new_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, response.data.get("state"))
