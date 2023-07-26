from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=28)
    surname = models.CharField(max_length=28)
    last_name = models.CharField(max_length=28)
    email = models.EmailField(max_length=50, blank=False, null=False)
    phone = models.CharField(max_length=12, null=False, blank=False)

    class Meta:
        """Creating a unique constraint for the email field"""
        constraints = [
            models.UniqueConstraint(name="%(app_label)s_%(class)s_name_unique",
                                    fields=["email"],)
        ]


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Level(models.Model):
    autumn = models.CharField(max_length=12, blank=True)
    spring = models.CharField(max_length=12, blank=True)
    summer = models.CharField(max_length=12, blank=True)
    winter = models.CharField(max_length=12, blank=True)


class Added(models.Model):
    STATUS = [
        ('NEW', 'new'),
        ('PEN', 'pending'),
        ('ACC', 'accepted'),
        ('REJ', 'rejected'),
    ]

    beautyTitle = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255, blank=True)
    connect = models.CharField(max_length=255, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUS, default='New')


class Images(models.Model):
    added = models.ForeignKey(Added, on_delete=models.CASCADE,
                              related_name='images')
    images = models.URLField()
    title = models.CharField(max_length=255)
