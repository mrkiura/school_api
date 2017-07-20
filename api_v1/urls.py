from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet, StudentViewSet

router = DefaultRouter()

router.register('schools', SchoolViewSet)
router.register('students', StudentViewSet)

urlpatterns = router.urls
