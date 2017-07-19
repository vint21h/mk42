# -*- coding: utf-8 -*-

# mk42
# mk42/apps/users/signals/user.py

from __future__ import unicode_literals


__all__ = [
    "post_save_user",
]


def post_save_user(sender, instance, created, **kwargs):
    """
    Send email notification after user registration.

    :param sender: sender model class.
    :type sender: object.
    :param instance: user model instance.
    :type instance: mk42.apps.users.models.user.User.
    :param created: is model instance created/edited.
    :type created: bool
    :param kwargs: additional args.
    :type kwargs: dict.
    """

    if created:

        instance.send_registration_email()
