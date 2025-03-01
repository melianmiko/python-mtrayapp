Release Notes
=============

v1.0.0 (2022-03-27) - First fork release
----------------------------------------
* Added OOP features for Menu object
* Added message, error, confirm dialgos
* Removed xorg and gtk backends
* Added ability to use file path as icon
* (darwin backend was broken, for now)

v0.19.3 (2022-03-18) - Various fixes
------------------------------------
*  Do not crash when passed a ``None`` menu.
*  Only let ``pystray.Icon.stop`` block for 5 seconds when waiting for the
   ``setup`` function to complete.
*  Made usage example single, runnable script.


v0.19.2 (2022-01-01) - Allow tuple as menu argument
---------------------------------------------------
*  Corrected menu implementation to allow tuples as arguments as indicated by
   the documentation.


v0.19.1 (2021-12-06) - Simplify packaging
-----------------------------------------
*  Simplify loading of backends to make packaging into a standalone package
   easier.
*  Added release dates to release notes.


v0.19.0 (2021-12-05) - Ayatana AppIndicator support
---------------------------------------------------
*  Added support for *Ayatana AppIndicator* under *Linux*. Thanks to *Paulo
   Martinez*!
*  Corrected support for ``run_detached`` under *Linux* and *Windows*.


v0.18.0 (2021-10-20) - Easier integration with other libraries
--------------------------------------------------------------
*  Added a detached run mode to enable integration with libraries with a run
   loop. Thanks to *PySimpleGUI* and *glight2000* for their testing efforts!
*  Do not crash when running the icon in a non-main thread when using a *GTK+*
   backend.
*  Updated documentation.


v0.17.4 (2021-06-26) - Corrected import on Windows
--------------------------------------------------
*  Corrected imports from _WinDLL_ to ensure argument definitions are private
   to this library. Thanks to *TomsonBoylett*!


v0.17.3 (2021-04-02) - macOS and AppIndicator bug fixes
-------------------------------------------------------
*  Let the default timeout for notifications when using the *AppIndicator*
   backend be decided by the desktop environment, not infinity. Thanks to
   *Angelo Naselli*!
*  Do not attempt to create a menu before the icon has started on *macOS*.


v0.17.2 (2020-12-02) - Windows bug fixes
----------------------------------------
*  Actually release loaded icons on *Windows*. Thanks to *Bob1011941*!
*  Let mouse button release trigger menu and action on *Windows* as expected.
   Thanks to *Ennea*!


v0.17.1 (2020-08-30) - Corrected release notes
----------------------------------------------
*  Corrected attribution of *Windows* notification fix.


v0.17.0 (2020-08-30) - Various bug fixes
----------------------------------------
*  Corrected signalling in *GTK* backend. Thanks to *Simon Lindholm*!
*  Corrected hinding of notification message in *GTK backend*. Thanks to *Simon
   Lindholm*!
*  Corrected notification structure on *Windows*. Thanks to *flameiguana*!


v0.16.0 (2020-06-09) - Enable notifications
-------------------------------------------
*  Added support for notifications. Thanks to *ralphwetzel* and *Chr0nicT*!
*  Added support for forcing the backend to use.


v0.15.0 (2019-12-04) - Allow methods as menu callbacks
------------------------------------------------------
*  Allow passing a method as menu callback.
*  Ensure that the temporary file is removed when running under *AppIndicator*.
   Thanks to *superjamie*!


v0.14.4 (2018-09-18) - Allow setting icon after construction
------------------------------------------------------------
*  Do not require setting ``icon`` twice when not passing the icon to the
   constructor.
*  Clarified documentation regarding name of menu argument.


v0.14.3 (2017-03-29) - Full license coverage
--------------------------------------------
*  Added license preamble to all source files. Thanks to *Björn Esser*!


v0.14.2 (2017-03-27) - Proper license files
-------------------------------------------
*  Added proper license files. Thanks to *Björn Esser*!


v0.14.1 (2017-03-05) - Restore icon after *explorer.exe* crash
--------------------------------------------------------------
*  Restore the icon when *explorer exe* restarts after a crash. Thanks to
   *Michael Dubner*!


v0.14 (2017-02-23) - Disabled menu items
----------------------------------------
*  Added support for disabling menu items.


v0.13 (2017-02-18) - Corrections for X
--------------------------------------
*  Make sure to set window size hints on *X*. Thanks to *filonenko-mikhail*!


v0.12 (2017-01-21) - Simplified API
-----------------------------------
*  Do not require use of ``setup`` to show icon.
*  Pass reference to menu item to action handler. If action handlers do not
   support this argument, they will be wrapped.
*  Updated documentation.


v0.11 (2016-12-05) - Radio buttons
----------------------------------
*  Added support for radio buttons.
*  Corrected transparent icons for *OSX*.


v0.10 (2016-09-27) - Changed Xlib backend library
-------------------------------------------------
*  Changed *Xlib* library.
*  Corrected test with incorrect parameter.


v0.9 (2016-09-26) - Submenus
----------------------------
*  Added support for nested menus.


v0.8 (2016-09-21) - Platform independent API and checkable
----------------------------------------------------------
*  Added method to explicitly update menu to enable support for other platforms.
*  Added support for *AppIndicator* backend.
*  Re-added native clickability for *OSX*.
*  Added support for check boxes.


v0.7 (2016-08-24) - Dynamic menus
---------------------------------
*  Added support for dynamically generating menu item properties when a popup
   menu is displayed.
*  Display the default menu item distinctly.
*  Changed the menu item API slightly.
*  Corrected logging on Windows.


v0.6 (2016-08-21) - Simplified API
----------------------------------
*  Removed explicit default action parameter ``on_activate``.
*  Allow terminating the application with *ctrl+c* on *OSX*.
*  Added basic logging.


v0.5 (2016-08-16) - Menu support
--------------------------------
*  Added support for popup menus.
*  Corrected bug which prevented stopping the icon on *Windows*.
*  Corrected documentation.


v0.4 (2016-08-05) - GTK+ 3 support
----------------------------------
*  Added support for *GTK+* on *Linux*.


v0.3.5 (2016-06-21) - Corrected import errors
---------------------------------------------
*  Propagate import errors raised on Linux to help troubleshoot missing
   ``Xlib`` module. Thanks to Lance Kindle!
*  Properly declare ``six`` as a dependency.
*  Declare ``python3-xlib`` as dependency on *Linux* for *Python 3*.


v0.3.4 (2016-05-24) - Corrected Python 3 issues on Xorg
-------------------------------------------------------
*  Make sure that ``pystray`` can be used on *Python 3* on *Xorg*.
*  Make sure the release making script runs on *Python 3*.


v0.3.3 (2016-04-21) - Corrected encoding issues
-----------------------------------------------
*  Make sure building works even when default encoding is not *utf-8*.
*  Corrected issue with click selector on *OSX*.


v0.3.2 (2016-04-19) - Universal wheel
-------------------------------------
*  Make sure to build a universal wheel for all python versions.


v0.3.1 (2016-04-10) - No-change packaging update
------------------------------------------------
*  Do not package an old version of ``pynput``.


v0.3 (2016-04-05) - Proper Python 3 Support
-------------------------------------------
*  Corrected Python 3 bugs.
*  Made ``Icon.run()`` mandatory on all platforms.


v0.2 (2016-03-27) - Initial Release
-----------------------------------
*  Support for adding a system tray icon on *Linux*, *Mac OSX* and *Windows*.
