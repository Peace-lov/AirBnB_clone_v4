#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ['3.86.13.91', '54.173.199.160']


def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.

    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for x in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for z in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [z for z in archives if "web_static_" in z]
        [archives.pop() for x in range(number)]
        [run("rm -rf ./{}".format(a)) for z in archives]
