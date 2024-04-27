#!/usr/bin/python3
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ['3.86.13.91', '54.173.199.160']


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dtx = datetime.utcnow()
    pkfile = "versions/web_static_{}{}{}{}{}{}.tgz".format(dtx.year,
                                                           dtx.month,
                                                           dtx.day,
                                                           dtx.hour,
                                                           dtx.minute,
                                                           dtx.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(pkfile)).failed is True:
        return None
    return pkfile


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        False if file_name does not exist
    """
    if os.path.isfile(archive_path) is False:
        return False
    file_x = archive_path.split("/")[-1]
    name = file_x.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file_x)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file_x, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file_x)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
