#!/usr/bin/env python3
"""API views for Listing and Booking."""

from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer


class ListingViewSet(viewsets.ModelViewSet):
    """ViewSet for managing travel listings."""
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """ViewSet for managing user bookings."""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
