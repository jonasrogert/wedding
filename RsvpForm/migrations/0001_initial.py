# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rsvp',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Full name')),
                ('email', models.EmailField(max_length=75, blank=True, help_text='Your email address where we can reach you.', null=True, verbose_name='Email')),
                ('telephone_number', models.CharField(max_length=20, blank=True, help_text='Telephone number either landline or mobile that we or             toasmaster can use to reach you', null=True, verbose_name='Telephone number')),
                ('food_preference', models.CharField(max_length=300, blank=True, help_text='Are you vegetarian or have any food allergies?', verbose_name='Special food')),
                ('next_day', models.BooleanField(default=False, help_text='We would really like you to join us for the day after                brunch!', verbose_name='Day after brunch')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
