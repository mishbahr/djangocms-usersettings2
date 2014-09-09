============
Installation
============

1. Install ``djangocms-usersettings2``::

    pip install djangocms-usersettings2


2. Add ``sites``, ``usersettings`` and ``djangocms_usersettings2`` to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'sites'
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


PLEASE NOTE: This project requires django CMS 3.0 or higher to be properly installed and configured. When
installing the``djangocms-usersettings2`` using pip, ``django-usersettings2`` will also be installed automatically.
