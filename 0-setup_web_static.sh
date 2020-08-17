#!/usr/bin/env bash
# Install nginx and prepare server for web_static

apt-get -y update
apt-get -y install nginx
mkdir /data
mkdir /data/web_static/
mkdir /data/web_static/releases/
mkdir /data/web_static/shared/
mkdir /data/web_static/releases/test/
echo "Testing Nginx config" > /data/web_static/releases/test/index.html
ln -sfn data/web_static/current /data/web_static/releases/test
chown ubuntu:nginx /data/
chown g+x /data/
sed -i "/listen 80 default_server;/a rewrite ^/hbnb_static /data/web_static/current/ permanent;" /etc/nginx/sites-available/default
service nginx restart
