from gi.repository import Nautilus, GObject, Gtk
from urlparse import urlparse
import os
import string
class DiskUsageLocationWidget(GObject.GObject, Nautilus.LocationWidgetProvider):
    def __init__(self):
        pass


    def get_mount_point(self,pathname):
        "Get the mount point of the filesystem containing pathname"
        pathname= os.path.normcase(os.path.realpath(pathname))
        parent_device= path_device= os.stat(pathname).st_dev
        while parent_device == path_device:
            mount_point= pathname
            pathname= os.path.dirname(pathname)
            if pathname == mount_point: break
            parent_device= os.stat(pathname).st_dev
        return mount_point

    def get_mounted_device(self,pathname):
        "Get the device mounted at pathname"
        # uses "/proc/mounts"
        pathname= os.path.normcase(pathname) # might be unnecessary here
        try:
            with open("/proc/mounts", "r") as ifp:
                for line in ifp:
                    fields= line.rstrip('\n').split()
                    # note that line above assumes that
                    # no mount points contain whitespace
                    if fields[1] == pathname:
                        return fields[0]
        except EnvironmentError:
            pass
        return None # explicit

    def get_fs_freespace(self,pathname):
        "Get the free space of the filesystem containing pathname"
        stat= os.statvfs(pathname)
        # use f_bfree for superuser, or f_bavail if filesystem
        # has reserved space for superuser
        return stat.f_bavail*stat.f_bsize

    def get_widget(self, uri, window):
        if type(window).__name__ == "NautilusDesktopWindow" :
            return None
        entry = Gtk.Entry()
        full_url = urlparse(uri)
        file_url = full_url.path
        file_url_no_special_whitespace_chars = string.replace(file_url, '%20', ' ')
        disk_free = self.get_fs_freespace(file_url_no_special_whitespace_chars)
        disk_free_gb = round(disk_free / 1024 / 1024 / 1024.0, 2)
        string_output = "Disk free: " + str(disk_free_gb) + " GB"
        entry.set_text(string_output)
        entry.show()
        return entry
