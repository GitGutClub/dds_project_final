from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self): return self.name

class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self): return self.name

class Category(models.Model):
    name = models.CharField(max_length=150)
    type = models.ForeignKey(Type, related_name='categories', on_delete=models.CASCADE)
    class Meta:
        unique_together = ('name','type')
    def __str__(self): return f"{self.name} ({self.type})"

class Subcategory(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    class Meta:
        unique_together = ('name','category')
    def __str__(self): return f"{self.name} ({self.category.name})"

class Record(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    date = models.DateField(default=timezone.now)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='records')
    type = models.ForeignKey(Type, on_delete=models.PROTECT, related_name='records')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='records')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT, related_name='records')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField(blank=True, null=True)

    def clean(self):
        if self.category.type_id != self.type_id:
            raise ValidationError('Категория не относится к выбранному типу.')
        if self.subcategory.category_id != self.category_id:
            raise ValidationError('Подкатегория не относится к выбранной категории.')
        if self.amount is None:
            raise ValidationError('Сумма обязательна.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.date} | {self.type} | {self.category}/{self.subcategory} | {self.amount}"