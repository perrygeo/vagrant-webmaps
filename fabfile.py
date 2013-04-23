from fabric.api import *

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
    """
    Restart all map services to ensure config file changes are recognized
    """
    run('sudo service uwsgi restart && sudo service uwsgi status tilestache')
    run('sudo service nginx restart && sudo service nginx status')
    run('sudo stop tilemill && sudo start tilemill && sudo status tilemill')


def runserver():
    """
    Run the test tilestache server for debugging; port 8080 or :8088/test/
    """
    run("cd /usr/local/app/tilestache && tilestache-server.py tilestache.cfg")


def tail_log():
    """
    Watch the tilestache logs
    """
    run("sudo tail -f /var/log/uwsgi/app/tilestache.log")


def clear_layer(layername=None):
    """
    Delete keys for a given layer; `clear_layer:test_countries`"
    """
    if layername is None:
        print "Need a layername; try `clear_layer:test_countries`"
        return False

    run('redis-cli KEYS "*%s*" | xargs redis-cli DEL' % layername)


def clear_cache():
    """
    Clears ALL the data from the cache. You've been warned.
    """
    run("redis-cli FLUSHALL")


def redis_memory():
    """
    Show the memory used by the redis cache
    """
    run("redis-cli INFO | grep used_memory")


def reconfigure():
    """
    Looks for new mapnik xml files and creates new config files (also runs 'restart_services')
    """
    run("python /usr/local/app/scripts/reconfigure_maps.py")
    restart_services()
