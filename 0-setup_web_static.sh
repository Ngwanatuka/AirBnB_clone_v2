#!/usr/bin/env bash
# This script sets up the web servers for the deployment of web_static.

# Install Nginx if not already installed
if ! command -v nginx >/dev/null 2>&1; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary directories if they don't exist
web_static_dir="/data/web_static"
releases_dir="$web_static_dir/releases"
shared_dir="$web_static_dir/shared"
test_dir="$releases_dir/test"

mkdir -p "$test_dir" "$shared_dir"
touch "$test_dir/index.html"

# Create or recreate symbolic link
current_link="/data/web_static/current"
if [ -L "$current_link" ]; then
    sudo rm "$current_link"
fi
sudo ln -s "$test_dir" "$current_link"

# Set ownership of /data/ folder recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
#setting up the page to be served
sed -i '/^\tlocation \/ {$/a \ \tlocation /hbnb_static/ {\n\t\t\talias /data/web_static/current/;\n\t\t}\n' "$config_file"

# Restart Nginx to apply changes
sudo service nginx restart
