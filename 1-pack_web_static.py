#!/usr/bin/python3
""" A Fabric Script that generates a .tgz archive from the
contents of the web_static folder of your AirBnb Clone.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ The Function that generates .tgz archive"""

    now = datetime.now()

    time = now.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local(f"tar -czvf versions/web_static_{time}.tgz web_static")

        return (f"versions/web_static_{time}.tgz")

    except Exception as e:
        return None
