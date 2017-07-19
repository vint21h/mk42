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


__all__ = [
    "api",
]


# custom views
group__my__active = GroupViewSet.as_view({"get": "my__active"})

api = [
    url(r"^api/group/my/active\.(?P<format>[a-z0-9]+)/?$", group__my__active, name="group--my--active"),
    url(r"^api/group/my/active/$", group__my__active, name="group--my--active"),
    url(r"^api/", include(router.urls)),
]
