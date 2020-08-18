#!/usr/bin/python3

from fabric.api import local
from fabric.api import env
from fabric.operations import run, put
from datetime import datetime
import os.path
from os import path

time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
tar_archive = "web_static_" + time_stamp + ".tgz"


def do_pack():
    """run fabric on local"""
    if path.exists('versions') is False:
        local("mkdir versions")
    local("tar -cvzf versions/{} web_static".format(tar_archive))


env.hosts = ["34.75.185.85", "34.73.88.228"]


def do_deploy(archive_path):
    """deploy to server"""
    if path.exists('versions') is False:
        return False
    try:
        put('versions/web_static_20200817213142.tgz', '/tmp/web_static_20200817213142.tgz')
        run("tar -xzvf /tmp/web_static_20200817213142.tgz \
            /data/web_static/releases/web_static_20200817213142")
        run("rm -rf /tmp/web_static_20200817213142.tgz")
        run("rm /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/web_static_20200817213142/ \
            /data/web_static/current")
        return True
    except Exception as e:
        return False
