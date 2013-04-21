# vagrant-webmaps

### Automated deployment of a full-featured tile server and editing environment

```
git clone https://github.com/perrygeo/vagrant-webmaps.git
cd vagrant-webmaps
vagrant up
# go get some coffee and come back in 30 minutes
# ....
# point your favorite browser to http://localhost:8088 
# and get working on those fast, beautiful web maps
```

* Builds your virtual server with a single command using Vagrant
* Automatically installs and configures software with Puppet
* Remote management with Fabric
* Allows you to edit maps with Tilemill web interface and the CartoCSS language
* Renders them with Mapnik
* Caches them with TileStache and Redis
* Serves them with uwsgi and nginx
* Allows you to view the maps in a web browser with the OpenLayers-based Madrona layer manager.

### Fabric 

Instead of ssh, just use local commands to interact with the remote server

 ```
$ fab --list
Available commands:

    all               Use all servers
    dev               Use development server settings
    prod              Use production server settings

    clear_cache       Clears ALL the data from the cache. You've been warned.
    clear_layer       Delete keys for a given layer; `clear_layer:test_countr...
    restart_services  Restart all map services to ensure config file changes ...
    runserver         Run the test tilestache server for debugging; port 8080...
    tail_log          Watch the tilestache logs

$ fab dev restart_services
```

### Notes 
Default password on tilemill is `user`:`pass`, for goodness sake change it. 
```
printf "newuser:$(openssl passwd -crypt newpassword)\n" > /usr/local/app/tilemill-passwords
```

This is a work in progress, probably not fully bulletproof yet. YMMV. 

To deploy anywhere other than localhost (no port forwarding available), you should follow
[this guide](http://mapbox.com/tilemill/docs/guides/ubuntu-service/#configuring_to_listen_for_public_traffic)
 to listening for external ip traffic. Automating this is a big **TODO** in order to get 
 this to deploy on EC2 using the vagrant AWS plugin.

