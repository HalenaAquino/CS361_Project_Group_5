# System Manual: Threat Intelligence Dashboard

## 1. Installation & Setup

### Prerequisites
- Python 3.8+
- PostgreSQL 
- Node.js and np
- Git
- OS:  Windows 10+

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-org/threat-intel-dashboard.git
   cd threat-intel-dashboard
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   cd frontend/
   npm install
   cd ..
   ```

3. **Configure Environment**
   Create a `.env` file:
   ```
   DB_HOST=localhost
   DB_USER=admin
   DB_PASS=yourpassword
   THREAT_API_KEY=your_api_key
   ```

4. **Initialize the Database**
   ```bash
   python scripts/init_db.py
   ```

5. **Run the Application**
   ```bash
   npm run build
   python app.py
   ```

## 2. How to Use the Threat Intelligence Dashboard

### Features
- **Live Feed**: Displays active threats in real-time
- **Filtering**: Search by IP, severity, threat type
- **Visualization**: Graphs, heatmaps, and trend charts
- **Alerts**: Configurable severity thresholds

### Navigation Guide
- **Dashboard**: Summary of current threats and incidents
- **Threat Logs**: Detail view of all detected threats
- **Mitigation Center**: Tracks automatic and manual responses

## 3. How Automated Mitigation Works

### Workflow
1. **Threat Detection** via real-time log scanning and external feeds
2. **Classification** based on severity scoring (rules or ML-based)
3. **Automated Actions**
   - IP blocking
   - Quarantine procedures
   - Notifications to analysts
4. **Logging** into audit trail for future review

### Optional Settings
- Toggle auto-mitigation per threat type
- Set approval requirement before auto-response

