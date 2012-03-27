from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin, Page, Placeholder

class LinksOfInterestPlugin(CMSPlugin):
    """
    Model for the settings when using the first n links plugin
    """
    page = models.ForeignKey(Page, verbose_name=_("page"))
    placeholder_name = models.CharField(_("placeholder name"), max_length=50)
    count = models.SmallIntegerField(_("count"), default=4)
    
    def clean(self):
        try:
            self.page.placeholders.get(slot=self.placeholder_name)
        except Placeholder.DoesNotExist:
            raise ValidationError, _("Placeholder name doesn't exist for this "
                                     "page")
