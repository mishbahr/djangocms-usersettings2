from django.core.urlresolvers import NoReverseMatch, reverse

from cms.toolbar.items import Break
from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool

from usersettings.shortcuts import get_usersettings_model

try:
    from django.contrib.admin.options import IS_POPUP_VAR
except ImportError:
    IS_POPUP_VAR = '_popup'


try:
    from cms.cms_toolbars import ADMIN_MENU_IDENTIFIER, USER_SETTINGS_BREAK
except ImportError:
    from cms.cms_toolbar import ADMIN_MENU_IDENTIFIER, USER_SETTINGS_BREAK



@toolbar_pool.register
class UserSettingsToolbar(CMSToolbar):

    def __init__(self, *args, **kwargs):
        super(UserSettingsToolbar, self).__init__(*args, **kwargs)
        self.model = get_usersettings_model()
        self.opts = self.model._meta

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(
            ADMIN_MENU_IDENTIFIER, self.current_site.name)
        position = admin_menu.find_first(
            Break, identifier=USER_SETTINGS_BREAK)

        try:
            usersettings_obj = self.model.objects.get(site_id=self.current_site.pk)
        except self.model.DoesNotExist:
            usersettings_obj = None

        app_label = self.opts.app_label
        try:
            model_name = self.opts.model_name
        except AttributeError:  # module_name alias removed in django 1.8
            model_name = self.opts.module_name

        try:
            if usersettings_obj:
                url = '%s?%s' % (
                    reverse('admin:%s_%s_change' % (app_label, model_name),
                        args=(usersettings_obj.pk,)), IS_POPUP_VAR)
            else:
                url = '%s?site_id=%s&%s' % (
                    reverse('admin:%s_%s_add' % (app_label, model_name)),
                    self.current_site.pk,
                    IS_POPUP_VAR)
        except NoReverseMatch:
            pass
        else:
            admin_menu.add_modal_item(
                self.opts.verbose_name, url, position=position+1)
            admin_menu.add_break('usersettings-break', position=position+2)
