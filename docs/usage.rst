========
Usage
========
``UserSettingsToolbar`` will be automatically loaded as long as the ``CMS_TOOLBARS`` is not set (or set to None).
Or you can add ``usersettings.cms_toolbar.UserSettingsToolbar`` to ``CMS_TOOLBARS`` settings::

    CMS_TOOLBARS = [
        # CMS Toolbars
        ...

        # djangocms-usersettings2 Toolbar
       'djangocms_usersettings2.cms_toolbar.UserSettingsToolbar',
    ]

