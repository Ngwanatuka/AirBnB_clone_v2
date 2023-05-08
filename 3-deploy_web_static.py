#!/usr/bin/python3
"""
Fabric script to distribute an archive
to web servers and perform deployment steps.
"""

from fabric.api import run, env, put, local
import os.path
from datetime import datetime

env.hosts = ['ubuntu@3.83.253.251', 'ubuntu@54.175.223.207']


def do_pack():
    """
    Function to generate a compressed archive
    """
    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        filename = "web_static_{}.tgz".format(timestamp)
        local("tar -cvzf versions/{} web_static".format(filename))
        return "versions/{}".format(filename)
    except Exception as e:
        print("An error occurred during archive creation:", str(e))
        return None


def do_deploy(archive_path):
    """Function to deploy code and compress it"""

    if not os.path.isfile(archive_path):
        return False

    try:
        compressed_file = archive_path.split("/")[-1]
        no_extension = compressed_file.split(".")[0]
        remote_path = "/data/web_static/releases/{}/".format(no_extension)
        sym_link = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(remote_path))
        run("sudo tar -xvzf /tmp/{} -C {}".format(
            compressed_file, remote_path))
        run("sudo rm /tmp/{}".format(compressed_file))
        run("sudo mv {}/web_static/* {}".format(remote_path, remote_path))
        run("sudo rm -rf {}/web_static".format(remote_path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf {} {}".format(remote_path, sym_link))
        return True
    except Exception as e:
        print("An error occurred during deployment:", str(e))
        return False


def deploy():
    """
    Function to create and distribute an archive to web service
    """

    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)
