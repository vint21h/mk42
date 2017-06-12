# -*- coding: utf-8 -*-

# mk42
# mk42/urls/common.py

from __future__ import unicode_literals

from django.conf.urls import include
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = []

# third part apps urls patterns
urlpatterns += [
    url(r"^robots\.txt", include("robots.urls")),
    url(r"^redactor/", include("redactor.urls")),
    url(r"^get-api-token/", obtain_auth_token, name="get-api-token"),
]

# third part apps i18n urls patterns
urlpatterns += i18n_patterns()

# django urls patterns
urlpatterns += [
    url(r"^i18n/", include("django.conf.urls.i18n")),
]

# django i18n urls patterns
urlpatterns += i18n_patterns(
    url(r"^admin/", include(admin.site.urls)),
)

# mk42 urls patterns
urlpatterns += []

# mk42 i18n urls patterns
urlpatterns += i18n_patterns()
