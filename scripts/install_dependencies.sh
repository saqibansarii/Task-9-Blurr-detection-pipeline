#!/bin/bash
cd /home/ubuntu/blur-detection

echo "Installing Python dependencies..."
pip3 install -r requirements.txt

echo "Setting permissions..."
chown -R ubuntu:ubuntu /home/ubuntu/myapp
