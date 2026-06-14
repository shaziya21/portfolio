# Portfolio

A modern, minimal portfolio site for Shaziya Akhtar with FastAPI backend, JWT authentication, and experience management.

## Setup

Requires Python 3.12+ (Ubuntu 24.04/25.04 default `python3` works).

```bash
cd portfolio
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

Open [http://localhost:8000](http://localhost:8000) for the portfolio.

## Admin

1. Go to [http://localhost:8000/signup](http://localhost:8000/signup) to create an account
2. Sign in at [http://localhost:8000/login](http://localhost:8000/login)
3. Manage experiences at [http://localhost:8000/dashboard](http://localhost:8000/dashboard)

## API

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/api/auth/signup` | No | Create account |
| POST | `/api/auth/login` | No | Get JWT token |
| GET | `/api/experiences` | No | List experiences |
| POST | `/api/experiences` | Yes | Add experience |
| PUT | `/api/experiences/{id}` | Yes | Update experience |
| DELETE | `/api/experiences/{id}` | Yes | Delete experience |

## Stack

- **Backend:** FastAPI, SQLAlchemy, SQLite, JWT
- **Frontend:** HTML, CSS, Jinja2 templates

## Deploy on AWS EC2

### 1. Launch EC2 instance

- **AMI:** Ubuntu 24.04 LTS
- **Instance type:** `t2.micro` or `t3.micro` (free tier)
- **Key pair:** Create/download a `.pem` file for SSH
- **Security group inbound rules:**
  - SSH (22) — your IP only
  - HTTP (80) — `0.0.0.0/0`
  - HTTPS (443) — `0.0.0.0/0` (if using SSL)

### 2. SSH into the instance

```bash
chmod 400 your-key.pem
ssh -i your-key.pem ubuntu@<EC2-PUBLIC-IP>
```

### 3. Run one-time setup

```bash
curl -fsSL https://raw.githubusercontent.com/shaziya21/portfolio/main/deploy/setup-ec2.sh -o setup-ec2.sh
chmod +x setup-ec2.sh
./setup-ec2.sh
```

Or clone manually and run:

```bash
git clone https://github.com/shaziya21/portfolio.git /var/www/portfolio
cd /var/www/portfolio
chmod +x deploy/setup-ec2.sh
./deploy/setup-ec2.sh
```

Your portfolio will be live at `http://<EC2-PUBLIC-IP>`.

### 4. Deploy updates later

```bash
cd /var/www/portfolio
./deploy/deploy.sh
```

### 5. Optional — custom domain + HTTPS

Point your domain's A record to the EC2 public IP, then on the server:

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d yourdomain.com
```

Update `server_name` in `/etc/nginx/sites-available/portfolio` to your domain before running certbot.

### Production layout

| Path | Purpose |
|------|---------|
| `/var/www/portfolio` | App code |
| `/var/lib/portfolio/portfolio.db` | SQLite database |
| `/var/www/portfolio/.env` | `SECRET_KEY`, `DATABASE_URL` |
| `/var/log/portfolio/` | Gunicorn logs |
