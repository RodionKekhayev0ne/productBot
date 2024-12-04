from django.db import models

# telegram_bot/models.py
from django.db import models


class User(models.Model):
    telegram_id = models.BigIntegerField(unique=True)  # Telegram ID пользователя
    username = models.CharField(max_length=255, null=True, blank=True)  # Имя пользователя Telegram
    first_name = models.CharField(max_length=255, null=True, blank=True)  # Имя пользователя
    last_name = models.CharField(max_length=255, null=True, blank=True)  # Фамилия пользователя
    is_registered = models.BooleanField(default=False)  # Флаг, чтобы узнать, зарегистрирован ли пользователь

    def __str__(self):
        return self.username or str(self.telegram_id)


class Product(models.Model):
    prodOwner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id")
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='products/images/')

    def __str__(self):
        return self.title
