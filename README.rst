DESCRIPTION
===========
This is a simple cms plugin that allows you to create a links of interest page
or links list in some placeholder.

Requirements
------------
Just django-cms 2.1+

Usage
-----
Just add 'cmsplugin_links_of_interest' to your INSTALLED_APPS, run syncdb or
migrate if you use south, and you're ready to go.

The idea of the plugin is that you create a page with a bunch of link plugins
laying around. This is better than sticking them into a TextPlugin because you
can see the links' titles, and reorder them with drag and drop. You leave this
page as not-published and then add a Links of Interest plugin where you want to
render them. You can override a template at `links_of_interest/links_list.html`
to fix how they render.

To print the n first links in a placeholder, just add that as the count
parameter. To print all of them, make count < 0
