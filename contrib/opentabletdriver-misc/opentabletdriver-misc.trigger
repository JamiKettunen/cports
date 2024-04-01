#!/bin/sh

# HACK: neither of these would never fly officially, just do whatever to make the setup convenient

# make /usr/lib/modprobe.d/99-opentabletdriver.conf go into effect immediately
/usr/bin/rmmod wacom hid_uclogic 2>/dev/null || :
# avoid loading the modules early in initramfs upon next reboot
# TODO: instead add some initramfs hook?
/usr/bin/update-initramfs -c -k all 2>/dev/null || :
