****************************
Mopidy-libNotify
****************************

.. image:: https://img.shields.io/pypi/v/Mopidy-libNotify.svg?style=flat
    :target: https://pypi.python.org/pypi/Mopidy-libNotify/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/travis/Mellich/mopidy-libnotify/master.svg?style=flat
    :target: https://travis-ci.org/Mellich/mopidy-libnotify
    :alt: Travis CI build status

.. image:: https://img.shields.io/coveralls/Mellich/mopidy-libnotify/master.svg?style=flat
   :target: https://coveralls.io/r/Mellich/mopidy-libnotify
   :alt: Test coverage

Adds notifications using libnotify. Supports artist, track title and album cover in notification.


Installation
============

Unfortunately, this extentions isn't available over pip, yet.
To install it on your system, clone the repository and switch into the direcotry.
Run the install script with::

    python setup.py install

This should install the extention globally on your system and integrate in mopidy.

Configuration
=============

Currently, no further configuration is necessary.
Like every other extention it can be disabled by setting::

    [libnotify]
    enabled = false

Project resources
=================

- `Source code <https://github.com/Mellich/mopidy-libnotify>`_
- `Issue tracker <https://github.com/Mellich/mopidy-libnotify/issues>`_


Credits
=======

- Original author: `Mellich <https://github.com/Mellich`__
- Current maintainer: `Mellich <https://github.com/Mellich`__
- `Contributors <https://github.com/Mellich/mopidy-libnotify/graphs/contributors>`_


Changelog
=========

v0.2.0 (UNRELEASED)
----------------------------------------

- added image support
- downloads the image to the ``/tmp/`` folder, if it is an URL

v0.1.0 (UNRELEASED)
----------------------------------------

- Initial release.
