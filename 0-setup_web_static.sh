#!/usr/bin/env bash
# This script sets up the web servers for the deployment of web_static.

# Install Nginx if not already installed
if ! command -v nginx >/dev/null 2>&1; then
    apt-get update
    apt-get install -y nginx
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
    rm "$current_link"
fi
ln -s "$test_dir" "$current_link"

# Set ownership of /data/ folder recursively
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
sed -i '/^\tlocation \/ {$/a'"$'\n''\t\tlocation /hbnb_static/ {\n\t\t\talias /data/web_static/current/;\n\t\t}'" "$config_file"

# Restart Nginx to apply changes
service nginx restart
