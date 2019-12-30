from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'computers', ComputerViewSet)
router.register(r'monitors', MonitorViewSet)
router.register(r'keyboards', KeyboardViewSet)
router.register(r'mouses', MouseViewSet)
router.register(r'office', OfficeViewSet)
router.register(r'os', OperatingSystemViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'responsible', ResponsibleViewSet)
router.register(r'towers', TowerViewSet)
router.register(r'brands', BrandViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
