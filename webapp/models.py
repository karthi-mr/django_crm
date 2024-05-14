from django.db import models


class Record(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.TextField(max_length=300)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    country = models.CharField(max_length=125)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.first_name}   {self.last_name}'