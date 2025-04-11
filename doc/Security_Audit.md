# Security Audit Report

**Date:** April 10, 2025  
**Target:** http://localhost:3000  
**Tools Used:**  
- Nmap v7.95  
- OWASP ZAP (AJAX Spider + Active Scan)

---

## 🔍 Nmap Scan Summary (Port 3000 Only)

**Command:**  
`nmap -p 3000 -A -T4 -oN nmap_3000_only.txt localhost`

**Findings:**
- Port `3000/tcp` is **open**
- Running a **Node.js Express** server
- App responds with title: **React App**
- No HTTPS/TLS in use

[NMap.txt](https://github.com/user-attachments/files/19697819/NMap.txt)


---

## 🕷️ OWASP ZAP Scan Summary

**Total Alerts:**  
- 🔶 Medium: 4  
- ⚠️ Low: 2  
- ℹ️ Informational: 2


### Medium Severity

- **CSP: Failure to Define Directive with No Fallback (6 instances)**  
  Content-Security-Policy is incomplete — missing `frame-ancestors`, `form-action`.  
  🔧 **Fix:** Set a full CSP policy with all key directives.

- **Content Security Policy Header Not Set (5 instances)**  
  App does not define a CSP header at all on key routes.  
  🔧 **Fix:** Set `Content-Security-Policy` headers via middleware like Helmet.

- **Cross-Domain Misconfiguration (10 instances)**  
  Server returns `Access-Control-Allow-Origin: *`, which allows cross-origin reads.  
  🔧 **Fix:** Restrict CORS headers to trusted domains.

- **Missing Anti-clickjacking Header (5 instances)**  
  App does not send `X-Frame-Options` or `frame-ancestors` in CSP.  
  🔧 **Fix:** Add `X-Frame-Options: DENY` or CSP equivalent.

### Low Severity

- **X-Content-Type-Options Header Missing (6 instances)**  
  🔧 **Fix:** Add `X-Content-Type-Options: nosniff` to all responses.

- **Leaking "X-Powered-By: Express" (10 instances)**  
  🔧 **Fix:** Disable `X-Powered-By` in Express (`app.disable('x-powered-by')`).

### Informational

- **Suspicious Comments Found**  
  A user-facing JS file (`bundle.js`) contains developer comments.  
  🔧 **Fix:** Remove or sanitize all frontend comments before deployment.

- **Modern Web App Detected**  
  React-based SPA detected, no issues, just ZAP noting it.



[2025-04-10-ZAP-Report-.md](https://github.com/user-attachments/files/19697830/2025-04-10-ZAP-Report-.md)

---

## ✅ Recommendations Summary

| Issue | Fix |
|---|---|
| ❌ No HTTPS | Add TLS via reverse proxy (e.g., Nginx + Certbot) |
| ❌ Missing CSP headers | Use `helmet` in Express to add CSP |
| ❌ Insecure CORS config | Restrict origins in `Access-Control-Allow-Origin` |
| ❌ Missing X-Frame-Options | Add `X-Frame-Options: DENY` |
| ❌ Server leaks headers | `app.disable('x-powered-by')` |
| ❌ Missing nosniff header | Add `X-Content-Type-Options: nosniff` |
| ❌ Exposed dev comments | Remove comments before build |


---

## 📦 Included Files in This Audit


