from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, QaViewSet

router = DefaultRouter()
router.register('category',CategoryViewSet,basename='category')
router.register('qa',QaViewSet,basename='qa')

urlpatterns = router.urls