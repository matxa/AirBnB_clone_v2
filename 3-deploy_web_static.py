#!/usr/bin/python3

from fabric.api import local
from fabric.api import env
from fabric.operations import run, put
from datetime import datetime
import os.path
from os import path


do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """deploy"""
    if not do_pack():
        return False
    b = do_deploy('versions/web_static_20200817213142.tgz')
    return b