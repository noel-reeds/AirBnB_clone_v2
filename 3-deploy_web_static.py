#!/usr/bin/python3
"""distributes an archive to your web servers"""
import re
import os
from fabric.api import run, sudo, env, put

env.user = "ubuntu"
env.hosts = ["18.207.218.204", "18.212.70.155"]


def do_pack():
    """check if versions dir exists and create."""
    if not os.path.isdir('./versions'):
        local("mkdir versions")
    _filepath = f"versions/web_static_{dt.now().strftime('%Y%m%d%H%M%S')}.tgz"
    local(f"tar -cvzf {_filepath} web_static")
    if not tarfile.is_tarfile(_filepath):
        return None
    else:
        print(f"web_static packed: {_filepath} \
-> {os.path.getsize(_filepath)}Bytes")
        return _filepath


def do_deploy(archive_path):
    """deploys web static pages"""
    try:
        os.path.isfile(archive_path)
        _archive_path = re.split('/', archive_path)[1].split('.')[0]
        _arch_name = archive_path.split('/')[1]
        put(archive_path, "/tmp/")
        run(f"mkdir /data/web_static/releases/{_archive_path}/")
        run(f"tar -xzf /tmp/{_arch_name} -C \
/data/web_static/releases/{_archive_path}/")
        run(f"mv /data/web_static/releases/{_archive_path}/\
web_static/* /data/web_static/releases/{_archive_path}/")
        run("rm -rf /tmp/{}".format(_arch_name))
        run("rm -rf /data/web_static/current")
        run(f"ln -s /data/web_static/releases/{_archive_path}/ \
/data/web_static/current")
        print("New version deployed!")
        return True
    except Exception as err:
        print(err)
        return False


def deploy():
    """ creates and distributes an archive to web servers"""
    # creates an archive of web static
    archive_path = do_pack()
    if not archive_path:
        return False
    else:
        ret = do_deploy(archive_path)
        return ret
