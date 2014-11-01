Nautilus-Status-Bar-Replacement
===============================
(c) 2014 Brunomag Concept SRL

www.brunomag.ro


Nautilus Python extension that shows in a textbox the disk space left when viewing a file or folder. This is a replacement of the old status bar that existed in previous versions of Nautilus 



Installation (on Ubuntu)
===============================
You copy the extension file DiskUsageLocationWidget.py in one of the following directories: /usr/share/nautilus-python/extensions/ or  ~/.local/share/nautilus-python/extensions/

In a terminal you kill nautilus with

$ nautilus -q


Afterwards you can relaunch it with

$ nautilus --no-desktop

or

$ nautilus -n
