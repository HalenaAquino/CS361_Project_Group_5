# Production Deployment Checklist (AWS)

## Environment Setup
- [x] Ubuntu 22.04 EC2 instance provisioned
- [x] Security Group allows ports 80, 443 (HTTPS), 5000 (internal only)

## Backend Setup
- [x] Flask API launched via PM2 (`pm2 start api.py`)
- [x] `.env` used for all secrets and keys
- [x] MySQL secured and bound to localhost

## Web & HTTPS
- [x] React app built using `npm run build`
- [x] Served via Nginx reverse proxy
- [x] HTTPS enabled using Certbot (Let's Encrypt)
- [x] Auto-renewal scheduled via `cron`

## Logging & Monitoring
- [x] `logrotate` configured for all backend logs
- [x] Uptime monitoring via UptimeRobot

## Final Steps
- [x] `git pull` latest commit from repository
- [x] Verified build and database connections
- [x] End-to-end system test passed
