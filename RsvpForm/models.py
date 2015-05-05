from django.db import models
from django.utils.translation import ugettext_lazy as _


class Rsvp(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name=_('Full name')
    )

    email = models.EmailField(
        blank=True, null=True, verbose_name=_('Email'),
        help_text=_('Your email address where we can reach you.')
    )

    telephone_number = models.CharField(
        max_length=20, blank=True, null=True,
        verbose_name=_('Telephone number'),
        help_text=_('Telephone number either landline or mobile that we or \
            toasmaster can use to reach you'),
    )

    food_preference = models.CharField(
        max_length=300, blank=True, verbose_name=_('Special food'),
        help_text=_('Are you vegetarian or have any food allergies?'),
    )

    next_day = models.BooleanField(
        default=False, verbose_name=_('Day after brunch'),
        help_text=_('We would really like you to join us for the day after\
                brunch!'),
    )

    def __str__(self):
        return self.name
