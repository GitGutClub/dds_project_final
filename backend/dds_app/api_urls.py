from rest_framework import routers
from .views import TypeViewSet, StatusViewSet, CategoryViewSet, SubcategoryViewSet, RecordViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('types', TypeViewSet)
router.register('statuses', StatusViewSet)
router.register('categories', CategoryViewSet)
router.register('subcategories', SubcategoryViewSet)
router.register('records', RecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
