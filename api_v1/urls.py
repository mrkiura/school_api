from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet

router = DefaultRouter()
router.register('schools', SchoolViewSet)

urlpatterns = router.urls
