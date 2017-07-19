# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/api/routers.py

from __future__ import unicode_literals

from rest_framework.routers import DefaultRouter

from mk42.apps.core.api.viewsets.group import GroupViewSet
from mk42.apps.core.api.viewsets.membership import MembershipViewSet
from mk42.apps.core.api.viewsets.event import EventViewSet
from mk42.apps.core.api.viewsets.rsvp import RSVPViewSet

router = DefaultRouter()

# registering viewsets
router.register(r"group", GroupViewSet)
router.register(r"membership", MembershipViewSet)
router.register(r"event", EventViewSet)
router.register(r"rsvp", RSVPViewSet)
