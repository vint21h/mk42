# mk42
# mk42/views/base.py

from __future__ import unicode_literals

from django.views.generic import TemplateView

__all__ = [
    "Index",
]


class Index(TemplateView):
    """
    Index view.
    """

    template_name = "mk42/index.html"
