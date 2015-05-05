from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from cms.app_base import CMSApp


class RsvpFormHook(CMSApp):
    name = _("Rsvp Form")
    urls = ["RsvpForm.urls"]
    app_name = 'RsvpForm'

apphook_pool.register(RsvpFormHook)
