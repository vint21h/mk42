# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/admin/membership.py

from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


__all__ = [
    "MembershipAdmin",
]


class MembershipAdmin(admin.ModelAdmin):
    """
    Customize Membership model for admin area.
    """

    list_display = ["id", "user", "group", "created", "active", ]
    list_filter = ["group", ]
    date_hierarchy = "created"
    readonly_fields = ["created", ]
    list_editable = ["active", ]
    fieldsets = (
        [None, {"fields": ["user", "group", ], }, ],
        [_("Other"), {"fields": ["created", "active", ], }, ],
    )

    def activate(self, request, queryset):
        """
        Make all selected memberships active.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param queryset: queryset with selected memberships.
        :type queryset: django.db.models.query.QuerySet.
        """

        queryset.update(active=True)

    activate.short_description = _("Activate selected memberships")

    def deactivate(self, request, queryset):
        """
        Deactivate all selected memberships.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param queryset: queryset with selected memberships.
        :type queryset: django.db.models.query.QuerySet.
        """

        queryset.update(active=False)

    deactivate.short_description = _("Deactivate selected memberships")
