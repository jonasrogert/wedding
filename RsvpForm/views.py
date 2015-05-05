from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from .forms import RsvpForm


class RsvpView(FormView):
    template_name = 'RsvpForm/rsvp.html'
    form_class = RsvpForm

    def form_valid(self, form, **kwargs):
        form.full_clean()
        print(form.cleaned_data)
        form.save()
        response = self.render_to_response(self.get_context_data(form=form))
        return response
