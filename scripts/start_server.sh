#!/bin/bash
cd /home/ubuntu/blur-detection

echo "Starting Gunicorn..."
systemctl start gunicorn
systemctl enable gunicorn

echo "Reloading Nginx..."
systemctl reload nginx

echo "Application started successfully."
