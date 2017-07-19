# -*- coding: utf-8 -*-

# mk42
# mk42/apps/users/models/user.py

from __future__ import unicode_literals
import uuid

from django.contrib.auth.models import AbstractUser
from django.utils.translation import (
    activate,
    get_language,
    ugettext_lazy as _,
)
from django.db import models
from django.contrib.sessions.models import Session
from django.conf import settings
from django.contrib.sites.models import Site
from django.db.models.signals import post_save

from templated_email import send_templated_mail

from avatar.templatetags.avatar_tags import avatar_url
from django_countries.fields import CountryField
from rest_framework.authtoken.models import Token

from mk42.apps.users.managers.user import UserManager
from mk42.apps.users.signals.user import post_save_user


__all__ = [
    "User",
]


class User(AbstractUser):
    """
    Custom user model.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("ID"))
    language = models.CharField(verbose_name=_("language"), max_length=5, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE)
    country = CountryField(verbose_name=_("country"), blank=True, null=True)

    FIELDS = ["id", "language", "country", ]

    def __unicode__(self):

        return getattr(self, self.USERNAME_FIELD)

    def __str__(self):

        return self.__unicode__()

    class Meta:

        app_label = "users"
        verbose_name = _("user")
        verbose_name_plural = _("users")

    objects = UserManager()

    def kick(self):
        """
        Clear all user sessions and API keys (logout from all logged in devices).
        """

        Token.objects.filter(user=self).delete()  # delete all user API keys

        sessions = Session.objects.all()

        for session in sessions:
            if session.get_decoded().get("_auth_user_id") == self.pk:
                session.delete()

    @property
    def avatar(self):
        """
        Return user avatar url.
        
        :return: user avatar url.
        :rtype: unicode.
        """

        return avatar_url(self)

    @property
    def email_context(self):
        """
        Return user emails default context.

        :return: default context for user emails.
        :rtype: dict.
        """

        return {
            "user": self,
            "site": Site.objects.get_current(),
            "FROM_EMAIL": settings.DEFAULT_FROM_EMAIL,
            "FROM_EMAIL_SENDER": settings.DEFAULT_FROM_EMAIL_SENDER,
            "FROM": "{sender} <{email}>".format(**{
                "sender": settings.DEFAULT_FROM_EMAIL_SENDER,
                "email": settings.DEFAULT_FROM_EMAIL,
            }),
            "protocol": settings.URL_PROTOCOL,
        }

    def send_email(self, template, context):
        """
        Send email to user.

        :param template: email template.
        :type template: unicode.
        :param context: email context.
        :type context: dict.
        """

        context.update(self.email_context)  # update email context by some default values
        language = get_language()  # remember current language (sometimes it's useful)
        activate(self.language)
        send_templated_mail(
            template_name=template,
            from_email=context.get("FROM", settings.DEFAULT_FROM_EMAIL),
            recipient_list=[self.email, ],
            context=context,
        )
        activate(language)

    def send_registration_email(self):
        """
        Send registration email to user.
        """

        self.send_email("registration", {})


# register signals
post_save.connect(post_save_user, sender=User)
