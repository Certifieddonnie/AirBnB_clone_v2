#!/usr/bin/python3
"""web server distribution
"""
from fabric.api import *
import tarfile
import os.path
import re
from datetime import datetime

env.hosts = ['35.175.130.79', '34.229.55.162']
env.user = 'ubuntu'
env.key_filename = "~/.ssh/school"


def do_pack():
    """distributes an archive to your web servers
    """
    target = local("mkdir -p ./versions")
    name = str(datetime.now()).replace(" ", '')
    opt = re.sub(r'[^\w\s]', '', name)
    tar = local('tar -cvzf versions/web_static_{}.tgz web_static'.format(opt))
    if os.path.exists("./versions/web_static_{}.tgz".format(opt)):
        return os.path.normpath("./versions/web_static_{}.tgz".format(opt))
    else:
        return None


# def do_deploy(archive_path):
#     """distributes an archive to your web servers
#     """
#     if os.path.exists(archive_path) is False:
#         return False
#     try:
#         arc = archive_path.split("/")
#         base = arc[1].strip('.tgz')
#         put(archive_path, '/tmp/')
#         sudo('mkdir -p /data/web_static/releases/{}'.format(base))
#         main = "/data/web_static/releases/{}".format(base)
#         sudo('tar -xzf /tmp/{} -C {}/'.format(arc[1], main))
#         sudo('rm /tmp/{}'.format(arc[1]))
#         sudo('mv {}/web_static/* {}/'.format(main, main))
#         sudo('rm -rf /data/web_static/current')
#         sudo('ln -s {}/ "/data/web_static/current"'.format(main))
#         return True
#     except Exception:
#         return False

def do_deploy(archive_path):
    """Deploy web files to server"""
    try:
        if not (path.exists(archive_path)):
            return False

        # upload archive
        put(archive_path, '/tmp/')
        # create target dir
        arc = archive_path.split("/")
        base = arc[-1].strip('.tgz')
        # timestamp = archive_path[-18:-4]
        sudo('mkdir -p /data/web_static/releases/{}/'
             .format(base))

        # uncompress archive and delete .tgz
        pat = '/data/web_static/releases/'
        sudo('tar -xzf /tmp/{0}.tgz -C {1}{0}/'.format(base, pat))

        # remove archive
        sudo('rm /tmp/{}.tgz'.format(base))

        # move contents into host web_static
        sudo('mv -f {1}{0}/web_static/* {1}{0}/'.format(base, pat))
        # remove extraneous web_static dir
        sudo('rm -rf {1}{0}/web_static'.format(base, pat))
        # delete pre-existing sym link
        sudo('rm -rf /data/web_static/current')

        # re-establish symbolic link
        sudo('sudo ln -s {1}{0} /data/web_static/current'.format(base, pat))
    except Exception as e:
        # print(e)
        return False


def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
