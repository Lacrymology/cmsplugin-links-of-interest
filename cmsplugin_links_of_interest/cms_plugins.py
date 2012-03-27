from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.plugins.utils import get_plugins

from cmsplugin_links_of_interest.models import LinksOfInterestPlugin

class CMSLinksOfInterestPlugin(CMSPluginBase):
    """
    Plugin that shows the first n LinkPlugin instances in a given page
    """
    model = LinksOfInterestPlugin
    name = _('Links of Interest')
    render_template = "plugins/links_of_interest.html"
    
    def render(self, context, instance, placeholder):
        """
        Render the latest entries
        """
        placeholder = instance.page.placeholders.get(
            slot=instance.placeholder_name)
        links = get_plugins(context["request"], placeholder).filter(
            plugin_type="LinkPlugin")
        if instance.count >= 0:
            links = links[:instance.count]

        context.update({
                'instance': instance,
                'links': links,
                'placeholder': placeholder,
                })
        return context

plugin_pool.register_plugin(CMSFirstLinksPlugin)
