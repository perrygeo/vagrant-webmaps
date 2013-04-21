# vagrant-webmaps

### Automated deployment of a full-featured tile server and editing environment

```
git clone https://github.com/perrygeo/vagrant-webmaps.git
cd vagrant-webmaps
vagrant up
# go get some coffee and come back in 20 minutes
# point your favorite browser to http://localhost:8088 and get to work
```

* Builds your virtual server with a single command using Vagrant
* Automatically installs and configures software with Puppet
* Allows you to edit maps with Tilemill web interface and the CartoCSS language
* Renders them with Mapnik
* Caches them with TileStache and Redis
* Serves with uwsgi and nginx
* Allows you to view the maps in a web browser with the OpenLayers-based Madrona layer manager.

# Notes 
Default password on tilemill is `user`:`pass`, for goodness sake change it. 
```
printf "newuser:$(openssl passwd -crypt newpassword)\n" > /usr/local/app/tilemill-passwords
```

This is a work in progress, probably not fully bulletproof yet. YMMV. 



