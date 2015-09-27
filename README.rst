=============================
djangocms-usersettings2
=============================


.. image:: http://img.shields.io/pypi/v/djangocms-usersettings2.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-usersettings2/
    :alt: Latest Version

.. image:: http://img.shields.io/pypi/dm/djangocms-usersettings2.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-usersettings2/
    :alt: Downloads

.. image:: http://img.shields.io/pypi/l/djangocms-usersettings2.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-usersettings2/
    :alt: License

.. image:: http://img.shields.io/coveralls/mishbahr/djangocms-usersettings2.svg?style=flat-square
  :target: https://coveralls.io/r/mishbahr/djangocms-usersettings2?branch=master


This package integrates `django-usersettings2 <https://github.com/mishbahr/django-usersettings2>`_ with `django-cms>=3.0 <https://github.com/divio/django-cms/>`_.

This allows a site editor to add/modify all ``usersettings`` in the frontend editing mode of django CMS
and provide your users with a streamlined editing experience.

This project requires django-usersettings2 and django CMS 3.0 or higher to be properly installed and configured. When
installing the ``djangocms-usersettings2`` using pip, ``django-usersettings2`` will also be installed automatically.

The full documentation for ``django-usersettings2`` is available at https://django-usersettings2.readthedocs.org.

Quickstart
----------

1. Install ``djangocms-usersettings2``::

    pip install djangocms-usersettings2


2. Add ``sites``, ``usersettings`` and ``djangocms_usersettings2`` to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'django.contrib.sites',
        'usersettings',
        'djangocms_usersettings2',
        ...
    )

3. ``UserSettingsToolbar`` will be automatically loaded as long as the ``CMS_TOOLBARS`` is not set (or set to None).
Or you can add ``usersettings.cms_toolbar.UserSettingsToolbar`` to ``CMS_TOOLBARS`` settings::

    CMS_TOOLBARS = [
        # CMS Toolbars
        ...

        # djangocms-usersettings2 Toolbar
       'djangocms_usersettings2.cms_toolbar.UserSettingsToolbar',
    ]

You may also like...
--------------------
* djangocms-disqus - https://github.com/mishbahr/djangocms-disqus
* djangocms-fbcomments - https://github.com/mishbahr/djangocms-fbcomments
* djangocms-forms — https://github.com/mishbahr/djangocms-forms
* djangocms-gmaps — https://github.com/mishbahr/djangocms-gmaps
* djangocms-instagram — https://github.com/mishbahr/djangocms-instagram
* djangocms-responsive-wrapper — https://github.com/mishbahr/djangocms-responsive-wrapper
* djangocms-twitter2 — https://github.com/mishbahr/djangocms-twitter2
