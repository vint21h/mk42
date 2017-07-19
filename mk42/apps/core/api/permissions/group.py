# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/api/permissions/group.py

from __future__ import unicode_literals

from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
)
from rest_framework.compat import is_authenticated

from mk42.constants import (
    POST,
    DELETE,
    PATCH,
)


__all__ = [
    "GroupPermissions",
]


class GroupPermissions(BasePermission):
    """
    Group permissions.
    """

    def has_permission(self, request, view):
        """
        List/create objects permission.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param view: view set.
        :type view: mk42.apps.core.api.viewsets.group.GroupViewset.
        :return: permission is granted.
        :rtype: bool.
        """

        if request.method in SAFE_METHODS:
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
            return True

        if all([request.method == POST, is_authenticated(request.user), ]):
            # Allow create groups only for authenticated users.
            return True

        if all([request.method == PATCH, is_authenticated(request.user), ]):
            # In futures steps of flow allow user edit self owned groups.
            return True

    def has_object_permission(self, request, view, obj):
        """
        Show/edit/delete object permission.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param view: view set.
        :type view: mk42.apps.core.api.viewsets.group.GroupsViewset.
        :param obj: group model instance.
        :type obj: mk42.apps.core.models.group.Group.
        :return: permission is granted.
        :rtype: bool.
        """

        if all([request.method == PATCH, obj.owner == request.user, ]):
            # Allow only owner edit groups.
            return True

        if request.method == DELETE:
            # Disallow delete groups by anyone.
            return False

        if request.method in SAFE_METHODS:
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
            return True
