#!/usr/bin/env bash
<<<<<<< HEAD
# Install nginX and configure the http header

sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

=======
# A Script that sets up your web servers for the deployment of web_static
# Installing Nginx
sudo apt-get -y update
sudo apt-get -y install nginx

# Create the folders
>>>>>>> 9fead4fb810359e3b0276f04670de1192276c9e0
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
<<<<<<< HEAD

sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

=======
sudo echo "<html>
<head>
<title>
AirBnb Clone
</title>
</head>
<body>
Welcome to AirBnb Clone
</body>
</html>" | sudo tee '/data/web_static/releases/test/index.html'

# Create a symbolic link
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Ownership of the folder
sudo chown -R ubuntu:ubuntu /data/

# Nginx Config to serve content
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# restart Nginx
>>>>>>> 9fead4fb810359e3b0276f04670de1192276c9e0
sudo service nginx restart
