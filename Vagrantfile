# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
  config.vm.box = "precise32"
  config.vm.box_url = "http://files.vagrantup.com/precise32.box"

  config.vm.forward_port 80, 8088
  config.vm.forward_port 20008, 20008
  config.vm.forward_port 20009, 20009
  config.vm.share_folder "v-app", "/usr/local/app", "./"

  config.vm.provision :puppet do |puppet|
    puppet.manifests_path = "puppet/manifests"
    puppet.manifest_file  = "app.pp"
    puppet.module_path = "puppet/modules"
    puppet.options = ["--templatedir","/vagrant/puppet/manifests/files", "--verbose"] #, "--debug"]
  end
end
