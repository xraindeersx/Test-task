from django.db import models


class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    category = models.CharField('category', max_length=100)
    description = models.TextField('Description', blank=True)
    price = models.DecimalField('Price', decimal_places=2, max_digits=8)
    general_note = models.CharField('general', max_length=500)
    special_note = models.CharField('special', max_length=500)
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)


    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
