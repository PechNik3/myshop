from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Ваши кастомные поля
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    # Переопределяем related_name для избегания конфликтов
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Убедитесь, что это имя уникально
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Убедитесь, что это имя уникально
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )
