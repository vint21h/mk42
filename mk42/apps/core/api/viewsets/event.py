# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/api/viewsets/event.py

from __future__ import unicode_literals

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from mk42.apps.core.models.event import Event
from mk42.apps.core.api.serializers.event import EventSerializer
from mk42.apps.core.api.permissions.event import EventPermissions
from mk42.lib.utils.pagination import ExtendedPageNumberPagination


__all__ = [
    "EventViewSet",
]


class EventViewSet(ModelViewSet):
    """
    Event view set.
    """

    queryset = Event.objects.all() 
    serializer_class = EventSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    pagination_class = ExtendedPageNumberPagination
    permission_classes = [EventPermissions, ]
    filter_fields = ["group", ]
    ordering_fields = ["created", "start", ]


