#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the web_static folder
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder.
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_" + now + ".tgz"
    archive_path = "versions/" + archive_name

    local("mkdir -p versions")

    try:
        local("tar -czvf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        return None
