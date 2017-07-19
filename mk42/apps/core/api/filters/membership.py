# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/api/filters/membership.py

from __future__ import unicode_literals

from django_filters.rest_framework import FilterSet

from mk42.apps.core.models.membership import Membership


__all__ = [
    "MembershipFilter",
]


class MembershipFilter(FilterSet):
    """
    Membership filter.
    """

    class Meta:

        model = Membership
        fields = ["user", "group", "active", ]
