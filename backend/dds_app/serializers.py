from rest_framework import serializers
from .models import Type, Status, Category, Subcategory, Record

class TypeSerializer(serializers.ModelSerializer):
    class Meta: model = Type; fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta: model = Status; fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta: model = Category; fields = '__all__'

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta: model = Subcategory; fields = '__all__'

class RecordSerializer(serializers.ModelSerializer):
    status_name = serializers.CharField(source='status.name', read_only=True)
    type_name = serializers.CharField(source='type.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    subcategory_name = serializers.CharField(source='subcategory.name', read_only=True)

    class Meta:
        model = Record
        fields = [
            'id',
            'created_at',
            'date',
            'amount',
            'comment',
            'status',
            'status_name',
            'type',
            'type_name',
            'category',
            'category_name',
            'subcategory',
            'subcategory_name',
        ]

    def validate(self, data):
        type_obj = data.get('type') or getattr(self.instance, 'type', None)
        category_obj = data.get('category') or getattr(self.instance, 'category', None)
        subcategory_obj = data.get('subcategory') or getattr(self.instance, 'subcategory', None)
        if category_obj and type_obj and category_obj.type_id != type_obj.id:
            raise serializers.ValidationError('Категория не принадлежит выбранному типу.')
        if subcategory_obj and category_obj and subcategory_obj.category_id != category_obj.id:
            raise serializers.ValidationError('Подкатегория не принадлежит выбранной категории.')
        if not data.get('amount') and not (self.instance and self.instance.amount):
            raise serializers.ValidationError('Сумма обязательна.')
        return data
