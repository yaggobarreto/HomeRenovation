from rest_framework.routers import DefaultRouter

from .api import ReformaItemViewSet

router = DefaultRouter()
router.register('itens', ReformaItemViewSet)

urlpatterns = router.urls
