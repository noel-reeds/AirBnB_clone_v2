#!/usr/bin/python3
"""creates an archive from web_static"""
import os, tarfile
from datetime import datetime as dt
from fabric.api import local, run

def do_pack():
    """check if versions dir exists and create."""
    if not os.path.isdir('./versions'):
        local("mkdir versions")
    _filepath = f"versions/web_static_{dt.now().strftime('%Y%m%d%H%M%S')}.tgz"
    local(f"tar -cvzf {_filepath} web_static")
    if not tarfile.is_tarfile(_filepath):
        return None
    else:
        print(f"web_static packed: {_filepath} -> {os.path.getsize(_filepath)}Bytes")
