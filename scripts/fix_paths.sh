#!/bin/bash

find /usr/local/app/xml/*.xml -type f | xargs sed -i \
  's/g:\\projects\\projects2011\\LandOwnerTools\\data\\Tilemill\\/\/usr\/local\/app\/data\/forestplanner\//gI'
