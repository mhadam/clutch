Configuration
-------------
By default, the RPC server listens at::

    http://localhost:9091/transmission/rpc

But this can be changed through configuration settings like ``rpc-bind-address`` and ``port``.

Other useful settings include ``rpc-whitelist`` (for whitelisting IP addresses), and ``rpc-host-whitelist`` (for whitelisting domain names).

GUI configuration
*****************

MacOS client
............
In the MacOS desktop client, these settings are accessed through the system menu bar:

:menuselection:`Transmission --> Preferences --> Remote`

File configuration
******************
Settings can be manually specified in a platform-specific file, as well.

Reference `Transmission's configuration file documentation`_ for all available settings, their default values, as well as where the configuration file is located for each platform.

.. _`Transmission's configuration file documentation`: https://github.com/transmission/transmission/wiki/Editing-Configuration-Files
