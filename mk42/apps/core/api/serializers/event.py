# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/api/serializers/event.py

from __future__ import unicode_literals

from rest_framework import serializers

from mk42.apps.core.models.event import Event


__all__ = [
    "EventSerializer",
]


class EventSerializer(serializers.ModelSerializer):
    """
    Event serializer.
    """

    class Meta:

        model = Event
        read_only_fields = [
            "created", 
            "updated",
        ]
        extra_kwargs = {
            "url": {"view_name": "core:event-detail", },
        }
        fields = [
            "id",
            "name",
            "description",
            "group",
            "address",
            "start",
            "created",
            "updated",
            "url",
        ]
