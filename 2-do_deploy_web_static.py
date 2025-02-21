#!/usr/bin/python3
"""distributes an archive to your web servers"""
import re
import os
from fabric.api import run, sudo, env, put

env.user = "ubuntu"
env.hosts = ["44.203.126.231", "52.91.254.211"]


def do_deploy(archive_path):
    """deploys web static pages"""
    try:
        os.path.isfile(archive_path)
        _archive_path = re.split('/', archive_path)[1].split('.')[0]
        _arch_name = archive_path.split('/')[1]
        put(archive_path, "/tmp/")
        run(f"mkdir /data/web_static/releases/{_archive_path}/")
        run(f"tar -xzf /tmp/{_arch_name} -C\
            /data/web_static/releases/{_archive_path}/")
        run("rm -rf /tmp/{_arch_name}")
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{_archive_path}/ \
            /data/web_static/current")
    except Exception as err:
        print(err)
