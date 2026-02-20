#!/bin/bash
echo "Stopping Gunicorn..."
if systemctl is-active --quiet gunicorn; then
    systemctl stop gunicorn
fi
echo "Server stopped."
