from rest_framework.routers import DefaultRouter

from online_platform.apps import OnlinePlatformConfig
from online_platform.views import ProviderViewSet, ProductViewSet, ContactViewSet

app_name = OnlinePlatformConfig.name

provider_router = DefaultRouter()
provider_router.register(r'providers', ProviderViewSet, basename='provider')

product_router = DefaultRouter()
product_router.register(r"product", ProductViewSet, basename="product")

contact_router = DefaultRouter()
contact_router.register(r"contact", ContactViewSet, basename="contact")


urlpatterns = [] + provider_router.urls + product_router.urls + contact_router.urls
