#!/usr/bin/python3

import os
from datetime import datetime
from fabric.api import local, runs_once, task

@runs_once
def do_pack():
    """
    Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack
    """
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    the_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(the_time.year, the_time.month, the_time.day, the_time.hour, the_time.minute, the_time.second)
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, size))
        return output
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    do_pack()

