from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny

from .models import Type, Status, Category, Subcategory, Record
from .serializers import (
    TypeSerializer, StatusSerializer, CategorySerializer,
    SubcategorySerializer, RecordSerializer
)


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class BaseViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)


class TypeViewSet(BaseViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class StatusViewSet(BaseViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class CategoryViewSet(BaseViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryViewSet(BaseViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class RecordViewSet(BaseViewSet):
    queryset = Record.objects.select_related(
        'status', 'type', 'category', 'subcategory'
    ).all().order_by('-date')
    serializer_class = RecordSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        status = self.request.GET.get('status')
        type_ = self.request.GET.get('type')
        category = self.request.GET.get('category')
        subcategory = self.request.GET.get('subcategory')

        if date_from:
            qs = qs.filter(date__gte=date_from)
        if date_to:
            qs = qs.filter(date__lte=date_to)
        if status:
            qs = qs.filter(status_id=status)
        if type_:
            qs = qs.filter(type_id=type_)
        if category:
            qs = qs.filter(category_id=category)
        if subcategory:
            qs = qs.filter(subcategory_id=subcategory)

        return qs

    @action(detail=False, methods=['get'])
    def totals(self, request):
        s = self.get_queryset().aggregate(total=Sum('amount'))
        return Response(s)
