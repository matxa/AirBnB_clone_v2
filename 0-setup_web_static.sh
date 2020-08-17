#!/usr/bin/env bash
# Install nginx and prepare server for web_static

sudo apt-get -y update
sudo apt-get -y install nginx
sudo sudo systemctl start nginx
sudo mkdir -p /data
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "<h1>Testing Nginx config</h1>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
LINE="location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tindex index.html;\n\t}"
sudo sed -i "54i $LINE" /etc/nginx/sites-available/default
sudo service nginx restart
