#!/usr/bin/python3
"""Compress web static package
"""
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['3.86.13.91', '54.173.199.160']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
        """Deploys web files into server
        """
        try:
                if not (path.exists(archive_path)):
                        return False

                # upload and transfers  archive
                put(archive_path, '/tmp/')

                # creates a target dir
                timest = archive_path[-18:-4]
                run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(timest))

                # Decompress archive and deletes .tgz
                run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
                    .format(timest, timest))

                # Delets archive
                run('sudo rm /tmp/web_static_{}.tgz'.format(timest))

                # Transfers contents into host web_static
                run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(timest, timest))

                # Delets extraneous web_static dir
                run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'
                    .format(timest))

                # deletes pre-existing symbolic link
                run('sudo rm -rf /data/web_static/current')

                # Re-establishes symbolic link
                run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(timest))
        except:
                return False

        # return True on success
        return True
