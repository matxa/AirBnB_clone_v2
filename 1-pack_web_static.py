#!/usr/bin/python3

from fabric.api import local
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
