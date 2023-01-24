#!/usr/bin/python3
""" A Fabric Script that generates a .tgz archive from the
contents of the web_static folder of your AirBnb Clone.
"""
from fabric.api import local
from time import strftime


def do_pack():
    """ The Function that generates .tgz archive"""

    time = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static".format(time))

        return ("versions/web_static_{}.tgz".format(time))

    except Exception as e:
        return None
