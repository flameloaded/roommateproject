from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, RequestViewSet, ListingRequestCreateView

router = DefaultRouter()
router.register(r'', ListingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('listings/<uuid:listing_id>/request/', ListingRequestCreateView.as_view(), name='listing-request'),
]
