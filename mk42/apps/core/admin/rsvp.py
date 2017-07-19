# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/admin/rsvp.py

from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


__all__ = [
    "RSVPAdmin",
]


class RSVPAdmin(admin.ModelAdmin):
    """
    Customize RSVP model for admin area.
    """

    list_display = ["id", "user", "event", "created", ]
    list_filter = ["event", ]
    date_hierarchy = "created"
    readonly_fields = ["created", ]
    fieldsets = (
        [None, {"fields": ["user", "event", ], }, ],
        [_("Other"), {"fields": ["created", ], }, ],
    )
