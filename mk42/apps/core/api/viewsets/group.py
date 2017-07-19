# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/api/viewsets/group.py

from __future__ import unicode_literals

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import list_route
from rest_framework.response import Response

from mk42.apps.core.models.group import Group
from mk42.apps.core.api.serializers.group import GroupSerializer
from mk42.apps.core.api.permissions.group import GroupPermissions
from mk42.apps.core.api.filters.group import GroupFilter
from mk42.lib.utils.pagination import ExtendedPageNumberPagination
from mk42.constants import GET


__all__ = [
    "GroupViewSet",
]


class GroupViewSet(ModelViewSet):
    """
    Group view set.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    ]
    pagination_class = ExtendedPageNumberPagination
    filter_class = GroupFilter
    permission_classes = [GroupPermissions, ]
    filter_fields = ["active", "owner", ]
    ordering_fields = ["name", "created", "updated", ]
    search_fields = ["name", ]

    def perform_create(self, serializer):
        """
        Override to set group owner.

        :param serializer: instance of group model serializer.
        :type serializer: mk42.apps.core.api.serializers.group.GroupSerializer.
        """

        defaults = {
            "owner": self.request.user,
        }

        serializer.save(**defaults)

    @list_route(methods=[GET, ])
    def my(self, request, **kwargs):
        """
        Return only user owned groups.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: serialized custom queryset response.
        :rtype: rest_framework.response.Response.
        """

        queryset = self.filter_queryset(queryset=Group.objects.filter(owner=request.user))
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    @list_route(methods=[GET, ])
    def active(self, request, **kwargs):
        """
        Return only active groups.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: serialized custom queryset response.
        :rtype: rest_framework.response.Response.
        """

        queryset = self.filter_queryset(queryset=Group.objects.active())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    @list_route(methods=[GET, ])
    def inactive(self, request, **kwargs):
        """
        Return only inactive groups.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: serialized custom queryset response.
        :rtype: rest_framework.response.Response.
        """

        queryset = self.filter_queryset(queryset=Group.objects.inactive())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    @list_route(methods=[GET, ])
    def my__active(self, request, **kwargs):
        """
        Return only active user owned groups.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: serialized custom queryset response.
        :rtype: rest_framework.response.Response.
        """

        queryset = self.filter_queryset(queryset=Group.objects.filter(owner=request.user).active())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
