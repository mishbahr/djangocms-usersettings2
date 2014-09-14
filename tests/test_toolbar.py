#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_djangocms-usersettings2
------------

Tests for `djangocms-usersettings2` toolbar module.
"""

from django.conf import settings
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.http import SimpleCookie
from django.core.urlresolvers import reverse
from django.utils.six import StringIO

try:
    from django.contrib.admin.options import IS_POPUP_VAR
except ImportError:
    IS_POPUP_VAR = '_popup'

from cms.toolbar.items import ModalItem
from cms.utils.compat.dj import force_unicode
from cms.cms_toolbar import ADMIN_MENU_IDENTIFIER
from cms.models import Page
from cms.utils.i18n import get_language_list

from usersettings.shortcuts import get_usersettings_model


class TestCMSToolbar(TestCase):

    request_factory = None
    user = None
    site = None
    languages = get_language_list()
    UserSettings = get_usersettings_model()

    usersettings_data = {
        'site_id': settings.SITE_ID,
        'user_id': 1,
        'site_title': 'Site Title',
        'tag_line': 'Friends don\'t let friends use Drupal',
        'street_address': '1600 Amphitheatre Parkway',
        'address_locality': 'Mountain View',
        'address_region': 'CA',
        'postal_code': '94043',
        'telephone': '+1 650-253-0000',
    }

    def setUp(self):
        self.request_factory = RequestFactory()
        self.site = Site.objects.get_or_create(id=settings.SITE_ID, domain='example.com', name='example.com')
        self.user = User.objects.create(username='admin', is_staff=True, is_superuser=True)

    def get_pages(self):
        from cms.api import create_page
        page = create_page(u'Page One', 'cms/pages/default.html', language='en-us')
        for lang in self.languages:
            page.publish(lang)
        return page.get_draft_object()

    def get_request(self, page, lang):
        request = self.request_factory.get(page.get_path(lang))
        request.current_page = page
        request.user = self.user
        request.session = {}
        request.cookies = SimpleCookie()
        request.errors = StringIO()
        request.LANGUAGE_CODE = lang
        return request

    def get_page_request(self, page, user, path=None, edit=False, lang_code='en'):
        from cms.middleware.toolbar import ToolbarMiddleware
        path = path or page and page.get_absolute_url(lang_code)
        if edit:
            path += '?edit'
        request = RequestFactory().get(path)
        request.session = {}
        request.user = user
        request.LANGUAGE_CODE = lang_code
        if edit:
            request.GET = {'edit': None}
        else:
            request.GET = {'edit_off': None}
        request.current_page = page
        mid = ToolbarMiddleware()
        mid.process_request(request)
        return request

    def test_toolbar(self):
        """
        Test that UserSettings toolbar are present for superuser
        """
        from cms.toolbar.toolbar import CMSToolbar
        page = self.get_pages()
        request = self.get_page_request(page, self.user, '/', edit=True)
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        admin_menu = toolbar.menus[ADMIN_MENU_IDENTIFIER]

        usersettings_model_opts = self.UserSettings._meta
        MENU_ITEM_TITLE = usersettings_model_opts.verbose_name

        self.assertEqual(len(admin_menu.find_items(
            ModalItem, name="%s ..." % force_unicode(MENU_ITEM_TITLE))), 1)

    def test_toolbar_with_no_current_usersettings(self):
        """
        Test that UserSettings toolbar item URL is for add_view for superuser
        if UserSettings doesn't exists for current site
        """
        from cms.toolbar.toolbar import CMSToolbar
        page = self.get_pages()
        request = self.get_page_request(page, self.user, '/', edit=True)
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        admin_menu = toolbar.menus[ADMIN_MENU_IDENTIFIER]

        usersettings_model_opts = self.UserSettings._meta
        MENU_ITEM_TITLE = usersettings_model_opts.verbose_name

        add_url = '%s?site_id=%s&%s' % (
            reverse('admin:%s_%s_add' % (
                usersettings_model_opts.app_label,
                usersettings_model_opts.module_name)),
           settings.SITE_ID, IS_POPUP_VAR)
        usersettings_menu = \
            admin_menu.find_items(ModalItem, name='%s ...' % force_unicode(MENU_ITEM_TITLE))

        self.assertEqual(add_url, usersettings_menu[0].item.url)

    def test_toolbar_with_an_existing_usersetting(self):
        """
        Test that UserSettings toolbar item URL is for change_view for superuser
        if UserSettings already exists for current site
        """
        usersettings_model_opts = self.UserSettings._meta
        usersettings_obj = self.UserSettings.objects.create(**self.usersettings_data)

        from cms.toolbar.toolbar import CMSToolbar
        page = self.get_pages()
        request = self.get_page_request(page, self.user, '/', edit=True)
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()

        admin_menu = toolbar.menus[ADMIN_MENU_IDENTIFIER]
        MENU_ITEM_TITLE = usersettings_model_opts.verbose_name

        change_url = '%s?%s' % (
            reverse('admin:%s_%s_change' % (
                usersettings_model_opts.app_label,
                usersettings_model_opts.module_name), args=(usersettings_obj.pk,)),
            IS_POPUP_VAR)

        usersettings_menu = \
            admin_menu.find_items(ModalItem, name='%s ...' % force_unicode(MENU_ITEM_TITLE))

        self.assertEqual(change_url, usersettings_menu[0].item.url)

    def tearDown(self):
        Page.objects.all().delete()
        self.UserSettings.objects.all().delete()


