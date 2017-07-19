# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/api/viewsets/rsvp.py

from __future__ import unicode_literals

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import list_route
from rest_framework.response import Response

from mk42.apps.core.models.rsvp import RSVP
from mk42.apps.core.api.serializers.rsvp import RSVPSerializer
from mk42.apps.core.api.permissions.rsvp import RSVPPermissions
from mk42.lib.utils.pagination import ExtendedPageNumberPagination
from mk42.constants import GET


__all__ = [
    "RSVPViewSet",
]


class RSVPViewSet(ModelViewSet):
    """
    RSVP view set.
    """

    queryset = RSVP.objects.all()
    serializer_class = RSVPSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    pagination_class = ExtendedPageNumberPagination
    permission_classes = [RSVPPermissions, ]
    filter_fields = ["user", "event", ]
    ordering_fields = ["created", ]

    def perform_create(self, serializer):
        """
        Override to set RSVP user.

        :param serializer: instance of RSVP model serializer.
        :type serializer: mk42.apps.core.api.serializers.rsvp.RSVPSerializer.
        """

        defaults = {
            "user": self.request.user,
        }

        serializer.save(**defaults)

    @list_route(methods=[GET, ])
    def my(self, request, **kwargs):
        """
        Return only user RSVP.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: serialized custom queryset response.
        :rtype: rest_framework.response.Response.
        """

        queryset = self.filter_queryset(queryset=RSVP.objects.filter(user=request.user))
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
