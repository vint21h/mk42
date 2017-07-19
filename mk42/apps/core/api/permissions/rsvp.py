# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/api/permissions/rsvp.py

from __future__ import unicode_literals

from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
)
from rest_framework.compat import is_authenticated

from mk42.constants import (
    POST,
    DELETE,
)


__all__ = [
    "RSVPPermissions",
]


class RSVPPermissions(BasePermission):
    """
    RSVP permissions.
    """

    def has_permission(self, request, view):
        """
        List/create objects permission.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param view: view set.
        :type view: mk42.apps.core.api.viewsets.rsvp.RSVPViewset.
        :return: permission is granted.
        :rtype: bool.
        """

        if request.method in SAFE_METHODS:
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
            return True

        if all([request.method == POST, is_authenticated(request.user), ]):
            # Allow join to event only for authenticated users.
            return True

        if request.method == DELETE:
            # In futures steps of flow allow user delete own RSVP.
            return True

    def has_object_permission(self, request, view, obj):
        """
        Show/edit/delete object permission.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param view: view set.
        :type view: mk42.apps.core.api.viewsets.event.EventViewSet.
        :param obj: group model instance.
        :type obj: mk42.apps.core.models.event.Event.
        :return: permission is granted.
        :rtype: bool.
        """

        if all([obj.user == request.user, request.method == DELETE, ]):
            # Allow only delete RSVP.
            return True

        if request.method in SAFE_METHODS:
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
            return True
