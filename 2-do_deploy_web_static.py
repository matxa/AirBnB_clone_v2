#!/usr/bin/python3

from fabric.api import *
import os.path
from os import path

env.hosts = ['34.75.185.85', '34.73.88.228']


def do_deploy(archive_path):
    """deploy to server"""
    if path.exists('versions') is False:
        return False
    f_no_ext = archive_path[archive_path.find('/') + 1:archive_path.find('.')]
    f_yes_ext = archive_path[archive_path.find('/') + 1:]
    put(archive_path, "/tmp/")
    run("sudo mkdir -p /data/web_static/releases/{}/".format(f_no_ext))
    run("sudo tar -xzvf /tmp/{} /data/web_static/{}".format(f_yes_ext, f_no_ext))
    run("sudo rm -rf /tmp/{}".format(f_yes_ext))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -sf /data/web_static/releases/{}/ \
        /data/web_static/current".format(f_no_ext))
    return True
