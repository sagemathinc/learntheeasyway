#!/bin/bash
source /etc/lsb-release && echo "deb http://download.rethinkdb.com/apt $DISTRIB_CODENAME main" | sudo tee /etc/apt/sources.list.d/rethinkdb.list
wget -qO- https://download.rethinkdb.com/apt/pubkey.gpg | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y rethinkdb
ABSOLUTE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
sudo cp $ABSOLUTE_DIR/nginx_default.txt /etc/nginx/sites-available/default
sudo cp $ABSOLUTE_DIR/ssl-params.conf /etc/nginx/snippets/ssl-params.conf
sudo cp $ABSOLUTE_DIR/self-signed.conf /etc/nginx/snippets/self-signed.conf
sudo service nginx restart
python $ABSOLUTE_DIR/configure_secrets.py