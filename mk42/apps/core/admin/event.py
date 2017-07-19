# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/admin/event.py

from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


__all__ = [
    "EventAdmin",
]


class EventAdmin(admin.ModelAdmin):
    """
    Customize Event model for admin area.
    """

    list_display = ["id", "name", "group", "address", "start", "created", "updated", ]
    list_filter = ["group", ]
    search_fields = ["id", "name", "description", ]
    date_hierarchy = "created"
    readonly_fields = ["created", "updated", ]
    fieldsets = (
        [None, {"fields": ["name", "description", "group", "address", "start"], }, ],
        [_("Other"), {"fields": ["created", "updated", ], }, ],
    )


