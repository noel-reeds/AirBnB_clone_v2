#!/usr/bin/env bash
# installs nginx ubuntu server

#server public ip address
ip_addr=$(curl -s ifconfig.me)

if [ ! -x /usr/sbin/nginx ]; then
    echo "nginx not installed.."
    echo "installing nginx.."
    sudo apt install curl gnupg2 ca-certificates lsb-release ubuntu-keyring
    curl https://nginx.org/keys/nginx_signing.key | gpg --dearmor \
        | sudo tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/null
    echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] \
    http://nginx.org/packages/ubuntu $(lsb_release -cs) nginx" \
        | sudo tee /etc/apt/sources.list.d/nginx.list

    sudo apt update -y
    sudo apt upgrade -y
    sudo apt install nginx -y
fi

# start nginx
sudo service nginx start

# create /data/ folders
if [ ! -d "/data/" ]; then
    sudo mkdir /data/
    sudo mkdir /data/web_static/
    sudo mkdir /data/web_static/releases/
    sudo mkdir /data/web_static/shared/
    sudo mkdir /data/web_static/releases/test/
    sudo touch /data/web_static/releases/test/index.html
fi

# creates a symlink
if [ -L "/data/web_static/current" ]; then
    # delete already existing symlink
    sudo rm /data/web_static/current
    sudo ln -s "/data/web_static/releases/test/" "/data/web_static/current"
else
    sudo ln -s "/data/web_static/releases/test/" "/data/web_static/current"
fi

# give ownership of the /data/ folder
sudo chown -R ubuntu:ubuntu /data/

# location directive to serve static content
dir="\tserver {\n\t\tlisten 80;\n\t\tserver_name $ip_addr localhost;\n\n\t\tlocation /hbnb_static {\n\t\t\talias /data/web_static/current/;\n\t\t\tautoindex off;\n\t\t\t}\n\t\t}\n"

# configure Nginx to serve /data/web_static/current/ to hbnb_static
sudo sed -i '31s/include/#include/' /etc/nginx/nginx.conf
sudo sed -i "15i\\$dir" /etc/nginx/nginx.conf
sudo sed -i 's/\t/    /g' /etc/nginx/nginx.conf

# restart nginx
sudo service nginx reload
