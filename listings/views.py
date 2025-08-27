from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Listing, Request
from .serializers import ListingSerializer, RequestSerializer
from django.shortcuts import get_object_or_404

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]


# Nested create request for a listing
class ListingRequestCreateView(generics.CreateAPIView):
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, listing_id):
        listing = get_object_or_404(Listing, listing_id=listing_id)
        data = {
            "listing": listing.listing_id,
            "seeker": request.user.user_id
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
