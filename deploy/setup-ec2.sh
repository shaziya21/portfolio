#!/usr/bin/env bash
# Run once on a fresh Ubuntu 22.04/24.04 EC2 instance (as ubuntu user with sudo).
set -euo pipefail

REPO_URL="${REPO_URL:-https://github.com/shaziya21/portfolio.git}"
APP_DIR="/var/www/portfolio"
DATA_DIR="/var/lib/portfolio"
LOG_DIR="/var/log/portfolio"

echo "==> Installing system packages..."
sudo apt-get update -y
sudo apt-get install -y python3.12 python3.12-venv python3-pip nginx git curl

PYTHON=python3.12
if ! command -v "$PYTHON" &>/dev/null; then
  echo "ERROR: python3.12 is required. Ubuntu 24.04+ should provide it via apt."
  exit 1
fi
echo "Using $($PYTHON --version)"

echo "==> Creating directories..."
sudo mkdir -p "$APP_DIR" "$DATA_DIR" "$LOG_DIR"
sudo chown -R ubuntu:ubuntu "$APP_DIR" "$DATA_DIR" "$LOG_DIR"

echo "==> Cloning repository..."
if [ ! -d "$APP_DIR/.git" ]; then
  git clone "$REPO_URL" "$APP_DIR"
else
  echo "Repo already exists at $APP_DIR — skipping clone."
fi

cd "$APP_DIR"

echo "==> Setting up Python virtual environment..."
rm -rf venv
$PYTHON -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "==> Creating environment file..."
if [ ! -f "$APP_DIR/.env" ]; then
  SECRET=$($PYTHON -c "import secrets; print(secrets.token_urlsafe(48))")
  cat > "$APP_DIR/.env" <<EOF
SECRET_KEY=$SECRET
DATABASE_URL=sqlite:////$DATA_DIR/portfolio.db
EOF
  echo "Created $APP_DIR/.env with a generated SECRET_KEY."
else
  echo ".env already exists — skipping."
fi

echo "==> Installing systemd service..."
sudo cp deploy/portfolio.service /etc/systemd/system/portfolio.service
sudo systemctl daemon-reload
sudo systemctl enable portfolio

echo "==> Configuring Nginx..."
sudo cp deploy/nginx.conf /etc/nginx/sites-available/portfolio
sudo ln -sf /etc/nginx/sites-available/portfolio /etc/nginx/sites-enabled/portfolio
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl enable nginx

echo "==> Starting services..."
sudo systemctl restart portfolio
sudo systemctl restart nginx

echo ""
echo "Deployment complete!"
echo "  App directory : $APP_DIR"
echo "  Database      : $DATA_DIR/portfolio.db"
echo "  Logs          : $LOG_DIR/"
echo ""
echo "Open http://<your-ec2-public-ip> in your browser."
echo ""
echo "Optional — enable HTTPS with a domain:"
echo "  sudo apt install certbot python3-certbot-nginx -y"
echo "  sudo certbot --nginx -d yourdomain.com"
