#!/usr/bin/env python2
import os
import sys
import socket

if __name__ == "__main__":
    if socket.gethostname() == 'PersonalSite':
    	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personalsite.settings.prod")
    else: 
    	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personalsite.settings.dev")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
