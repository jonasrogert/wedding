from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div, Fieldset
from django.utils.translation import ugettext_lazy as _

from .models import Rsvp


class RsvpForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-xs-12 col-sm-4 col-md-4'
        self.helper.field_class = 'col-xs-12 col-sm-8 col-md-8'
        self.helper.layout = Layout(
            Fieldset(
                'OSA formulär',
                'name',
                'email',
                'telephone_number',
                'food_preference',
                Div(
                    'next_day',
                    Submit('submit', _('Submit')),
                    css_class='col-sm-offset-4',
                ),
            )
        )

    class Meta:
        model = Rsvp
