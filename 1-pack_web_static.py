#!/usr/bin/python3

from fabric import task
from datetime import datetime
import os
@task
def do_pack(c):
    """
    Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack
    """
    if not os.path.isdir("virsion"):
        os.mkdir("virsion")
    the_time = datetime.now()
    output = "virsions/web_static_{}{}{}{}{}{}.tgz".format(the_time.year, the_time.month, the_time.day, the_time.hour, the_time.minute, the_time.second)
    try:
        print("Packing web_static to {}".format(output))
        local("tgz -cvzf {} web_static".format(output))
        size = os.stat(output).st_size
        print("web_static packed: {} -> {}Bytes".format(output, size))
    except Exception:
        output = None
    return output
