#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os

# Define the remote user and IP addresses of your servers
env.user = 'ubuntu'
env.hosts = ['<IP web-01>', '<IP web-02>']

def do_deploy(archive_path):
    """
    Distributes an archive to web servers and deploys it.
    """
    if not os.path.exists(archive_path):
        print("Error: Archive does not exist.")
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Extract the archive to the /data/web_static/releases/ directory
        filename = os.path.basename(archive_path)
        release_path = '/data/web_static/releases/{}'.format(filename[:-4])
        run('mkdir -p {}'.format(release_path))
        run('tar -xzf /tmp/{} -C {}'.format(filename, release_path))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(filename))

        # Move the contents of the archive to the release folder
        run('mv {}/web_static/* {}'.format(release_path, release_path))

        # Remove the empty web_static directory
        run('rm -rf {}/web_static'.format(release_path))

        # Remove the old symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('ln -s {} /data/web_static/current'.format(release_path))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Error: {}".format(e))
        return False

# Example usage:
if __name__ == "__main__":
    archive_path = 'versions/web_static_20170315003959.tgz'  # Update with your actual archive path
    do_deploy(archive_path)
