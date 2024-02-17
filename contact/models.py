from typing import Any
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

    name=models.CharField(max_length=50)
    def __str__(self) -> str:
        return f'{self.name}'

class Contact(models.Model):
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank = True)
    show = models.BooleanField(default = True)
    picture = models.ImageField(blank=True,upload_to='picture_%Y/%m/%d')
    category = models.ForeignKey(
        Category, 
        on_delete = models.SET_NULL,
        blank=True,
        null=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    def __repr__(self) -> str:
        return f'Nome: {self.first_name}, Sobrenome: {self.last_name}'