#!/usr/bin/env bash
# Run on EC2 after initial setup to pull latest code and restart.
set -euo pipefail

APP_DIR="/var/www/portfolio"

cd "$APP_DIR"
git pull origin main

rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

sudo systemctl restart portfolio
sudo systemctl status portfolio --no-pager

echo "Deployed successfully."
