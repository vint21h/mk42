# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/api/serializers/rsvp.py

from __future__ import unicode_literals

from rest_framework import serializers

from mk42.apps.core.models.rsvp import RSVP


__all__ = [
    "RSVPSerializer",
]


class RSVPSerializer(serializers.ModelSerializer):
    """
    RSVP serializer.
    """

    class Meta:

        model = RSVP
        read_only_fields = [
            "created",
        ]
        extra_kwargs = {
            "url": {"view_name": "core:rsvp-detail", },
        }
        fields = [
            "id",
            "user",
            "event",
            "created",
            "url",
        ]
