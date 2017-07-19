# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/api/permissions/event.py

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
    "EventPermissions",
]


class EventPermissions(BasePermission):
    """
    Event permissions.
    """

    def has_permission(self, request, view):
        """
        List/create objects permission.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param view: view set.
        :type view: mk42.apps.core.api.viewsets.event.EventViewset.
        :return: permission is granted.
        :rtype: bool.
        """

        if request.method in SAFE_METHODS:
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
            return True

        if all([request.method == POST, is_authenticated(request.user), ]):
            # Allow create events only for authenticated users.
            return True

        if request.method == PATCH:
            # In futures steps of flow allow user edit self owned events.
            return True

    def has_object_permission(self, request, view, obj):
        """
        Show/edit/delete object permission.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param view: view set.
        :type view: mk42.apps.core.api.viewsets.event.EventViewset.
        :param obj: event model instance.
        :type obj: mk42.apps.core.models.event.Event.
        :return: permission is granted.
        :rtype: bool.
        """

        if obj.group.owner == request.user:
            # Allow only group owner edit objects.
            return True

        if request.method == DELETE:
            # Disallow delete events by anyone.
            return False

        if request.method in SAFE_METHODS:
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
            return True
