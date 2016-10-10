#!/bin/bash
source /etc/lsb-release && echo "deb http://download.rethinkdb.com/apt $DISTRIB_CODENAME main" | sudo tee /etc/apt/sources.list.d/rethinkdb.list
wget -qO- https://download.rethinkdb.com/apt/pubkey.gpg | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y rethinkdb
ABSOLUTE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ ! -f /etc/ssl/private/nginx-selfsigned.key ]; then
    sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt -subj "/C=GB/ST=London/L=London/O=Global Security/OU=IT Department/CN=example.com"
    sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048
    sudo cp $ABSOLUTE_DIR/nginx_default.txt /etc/nginx/sites-available/default
    sudo cp $ABSOLUTE_DIR/ssl-params.conf /etc/nginx/snippets/ssl-params.conf
    sudo cp $ABSOLUTE_DIR/self-signed.conf /etc/nginx/snippets/self-signed.conf
fi
sudo service nginx restart
python $ABSOLUTE_DIR/configure_secrets.py