# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/urls/api.py

from __future__ import unicode_literals

from django.conf.urls import (
    url,
    include,
)

from mk42.apps.core.api.routers import router
from mk42.apps.core.api.viewsets.group import GroupViewSet
from mk42.apps.core.api.viewsets.membership import MembershipViewSet


__all__ = [
    "api",
]


# custom endpoints
# group
group__my__active = GroupViewSet.as_view({"get": "my__active"})
group__my__inactive = GroupViewSet.as_view({"get": "my__inactive"})
# membership
membership__my__active = MembershipViewSet.as_view({"get": "my__active"})
membership__my__inactive = MembershipViewSet.as_view({"get": "my__inactive"})

api = [
    url(r"^api/group/my/active\.(?P<format>[a-z0-9]+)/?$", group__my__active, name="group--my--active"),
    url(r"^api/group/my/active/$", group__my__active, name="group--my--active"),
    url(r"^api/group/my/inactive\.(?P<format>[a-z0-9]+)/?$", group__my__inactive, name="group--my--inactive"),
    url(r"^api/group/my/inactive/$", group__my__inactive, name="group--my--inactive"),
    url(r"^api/membership/my/active\.(?P<format>[a-z0-9]+)/?$", membership__my__active, name="membership--my--active"),
    url(r"^api/membership/my/active/$", membership__my__active, name="group--my--active"),
    url(r"^api/membership/my/inactive\.(?P<format>[a-z0-9]+)/?$", membership__my__inactive, name="membership--my--inactive"),
    url(r"^api/membership/my/inactive/$", membership__my__inactive, name="membership--my--inactive"),
    url(r"^api/", include(router.urls)),
]
