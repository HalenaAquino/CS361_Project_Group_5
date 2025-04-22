# Troubleshooting & Maintenance Guide

## Common Issues & Fixes

---

### 1. OSINT API Failure (e.g., Shodan, HaveIBeenPwned, VirusTotal)

**Symptoms:**  
- Risk scores not updated  
- Threat feed is empty  
- 403 / 429 errors from API  

**Possible Causes:**  
- Expired or invalid API key  
- Rate limit exceeded  
- Incorrect API endpoint  

**Fixes:**  
- Check logs 
- Validate API keys   
- Rotate to a backup API key  
- Run manual test using curl/Postman to confirm API status  

---

### 2. Database Connection Errors

**Symptoms:**  
- Backend server fails to start  
- 500 Internal Server Error on API calls  

**Possible Causes:**  
- Database service not running  
- Wrong DB credentials  
- Port conflict or blocked connection  

**Fixes:**  
- Restart the database service or container  
- Confirm DB credentials and port   
- Run test SQL queries manually to validate connectivity  

---

### 3. Frontend Dashboard Fails to Load

**Symptoms:**  
- Blank dashboard  
- Console shows network errors  

**Possible Causes:**  
- Backend API server is down  
- CORS errors  
- Incorrect API route  

**Fixes:**  
- Restart the backend server: `flask run` or `npm start`  
- Check that endpoint is working  
- Inspect browser console for specific JS or fetch errors  

---

### 4. Scheduled OSINT Data Not Updating

**Symptoms:**  
- No new threats appear every 6 hours  
- `fetch_osint.py` script not executing  

**Possible Causes:**  
- `schedule.run_pending()` not being called  
- Script not running as a background job  

**Fixes:**  
- Run the scheduler script manually and check output  
- Use a cron job or background process manager (e.g., PM2 or systemd)  

---

## System Maintenance Procedures

---

### Daily  
- Check logs: `/logs/`, `/logs/threat_events.log`, `/logs/api_errors.log`  
- Ensure OSINT updates ran successfully  
- Backup database (e.g., with `pg_dump`)  

### Weekly  
- Rotate API keys if rate limits are consistently reached  
- Test all API integrations manually  
- Run vulnerability scans (e.g., OWASP ZAP, Nmap)  

### Monthly  
- Perform full database backup  
- Validate restore from backup  
- Run performance test (JMeter or built-in testing)  
- Archive old threat logs  

---

## Best Practices

- Never commit `.env` files or secrets to Git  
- Use `.env.example` for structure sharing  
- Keep your GitHub issues board updated  
- Use semantic commit messages (e.g., `fix(api): handle token expiry`)  
- Document changes in `/docs/CHANGELOG.md`  
- Regularly update and patch dependencies (`pip freeze > requirements.txt`)  
- Enforce code reviews before merging pull requests  
