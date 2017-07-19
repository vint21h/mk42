# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/admin/group.py

from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


__all__ = [
    "GroupAdmin",
]


class GroupAdmin(admin.ModelAdmin):
    """
    Customize Group model for admin area.
    """

    list_display = ["id", "name", "owner", "created", "updated", "active", "slug", ]
    list_filter = ["owner", "active", ]
    search_fields = ["id", "name", ]
    date_hierarchy = "created"
    readonly_fields = ["created", "updated", ]
    list_editable = ["active", ]
    actions = ["activate", ]
    fieldsets = (
        [None, {"fields": ["name", "owner", "description", ], }, ],
        [_("Other"), {"fields": ["created", "updated", "active", "slug", ], }, ],
    )

    def activate(self, request, queryset):
        """
        Make all selected groups active.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param queryset: queryset with selected groups.
        :type queryset: django.db.models.query.QuerySet.
        """

        queryset.update(active=True)

    activate.short_description = _("Activate selected groups")

    def deactivate(self, request, queryset):
        """
        Deactivate all selected groups.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param queryset: queryset with selected groups.
        :type queryset: django.db.models.query.QuerySet.
        """

        queryset.update(active=False)

    deactivate.short_description = _("Deactivate selected groups")
