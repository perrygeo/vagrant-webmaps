from fabric.api import *
from fabric.contrib.files import exists
import time

vars = {
    # 'tomcat_version': '6.0.36'
}

env.forward_agent = True
env.key_filename = '~/.vagrant.d/insecure_private_key'


def dev():
    """ Use development server settings """
    servers = ['vagrant@127.0.0.1:2222']
    env.hosts = servers
    return servers


def prod():
    """ Use production server settings """
    servers = []
    env.hosts = servers
    return servers

def all():
    """ Use all servers """
    env.hosts = dev() + prod()


def restart_services():
    run('sudo service uwsgi restart && sudo service nginx restart')
