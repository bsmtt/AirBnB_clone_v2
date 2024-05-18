#!/usr/bin/python3
""" a module to package web_static files """
from datetime import datetime
import os
from fabric.api import local


def do_pack():
    """ package function """
    if not os.path.isdir("./versions"):
        os.makedirs("./versions")
    now_time = datetime.now().strftime("%Y%m%d%H%M%S")
    local("tar -czzf versions/web_static_{}.tgz web_static/*".format(now_time))
    return ("{}/versions/web_static_{}.tgz".format(os.path.dirname(
        os.path.abspath(__file__)), now_time))
