# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/api/viewsets/membership.py

from __future__ import unicode_literals

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import list_route
from rest_framework.response import Response

from mk42.apps.core.models.membership import Membership
from mk42.apps.core.api.serializers.membership import MembershipSerializer
from mk42.apps.core.api.permissions.membership import MembershipPermissions
from mk42.apps.core.api.filters.membership import MembershipFilter
from mk42.lib.utils.pagination import ExtendedPageNumberPagination
from mk42.constants import GET


__all__ = [
    "MembershipViewSet",
]


class MembershipViewSet(ModelViewSet):
    """
    Membership view set.
    """

    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    pagination_class = ExtendedPageNumberPagination
    filter_class = MembershipFilter
    permission_classes = [MembershipPermissions, ]
    filter_fields = ["user", "group", "active", ]
    ordering_fields = ["created", ]

    def perform_create(self, serializer):
        """
        Override to set membership user.

        :param serializer: instance of membership model serializer.
        :type serializer: mk42.apps.core.api.serializers.membership.MembershipSerializer.
        """

        defaults = {
            "user": self.request.user,
        }

        serializer.save(**defaults)

    @list_route(methods=[GET, ])
    def my(self, request, **kwargs):
        """
        Return only user memberships.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: serialized custom queryset response.
        :rtype: rest_framework.response.Response.
        """

        queryset = self.filter_queryset(queryset=Membership.objects.filter(user=request.user))
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    @list_route(methods=[GET, ])
    def active(self, request, **kwargs):
        """
        Return only active memberships.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: serialized custom queryset response.
        :rtype: rest_framework.response.Response.
        """

        queryset = self.filter_queryset(queryset=Membership.objects.active())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    @list_route(methods=[GET, ])
    def inactive(self, request, **kwargs):
        """
        Return only inactive memberships.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: serialized custom queryset response.
        :rtype: rest_framework.response.Response.
        """

        queryset = self.filter_queryset(queryset=Membership.objects.inactive())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
