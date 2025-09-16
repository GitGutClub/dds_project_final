from django.contrib import admin
from .models import Type, Status, Category, Subcategory, Record

admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Record)
