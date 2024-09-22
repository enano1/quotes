#!/bin/bash

if command -v python3 &>/dev/null; then
    echo "Python3 found, proceeding with pip installation..."
    python3 -m pip install -r requirements.txt
else
    echo "Python3 not found. Aborting."
    exit 1
fi

# Collect static files after pip installation
python3 manage.py collectstatic --noinput
