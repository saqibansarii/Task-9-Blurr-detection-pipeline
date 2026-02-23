#!/bin/bash
cd /home/ubuntu/myapp

echo "Starting Gunicorn..."
systemctl start gunicorn
systemctl enable gunicorn

echo "Reloading Nginx..."
systemctl reload nginx

echo "Application started successfully."
