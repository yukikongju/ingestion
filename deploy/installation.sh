#!/usr/bin/env bash
set -e

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

# Always activate it
source venv/bin/activate

# Upgrade pip inside the venv (safe!)
python -m pip install --upgrade pip

# Install requirements using venv’s pip
pip install -r requirements.txt
