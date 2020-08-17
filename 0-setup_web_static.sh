#!/usr/bin/env bash
# Install nginx and prepare server for web_static

apt-get -y update
apt-get -y install nginx
sudo systemctl start nginx
mkdir /data
mkdir /data/web_static/
mkdir /data/web_static/releases/
mkdir /data/web_static/shared/
mkdir /data/web_static/releases/test/
echo "<h1>Testing Nginx config</h1>" > /data/web_static/releases/test/index.html
ln -sfn data/web_static/current /data/web_static/releases/test
chown ubuntu:ubuntu /data/
chown g+x /data/
LINE="location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tindex index.html;\n\t}"
sed -r "54i $LINE" /etc/nginx/sites-available/default
service nginx restart
