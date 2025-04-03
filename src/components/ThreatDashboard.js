import React, { useState, useEffect } from "react";

const ThreatDashboard = () => {
  const [assets, setAssets] = useState([]);
  const [threats, setThreats] = useState([]);
  const [riskFilter, setRiskFilter] = useState(0);

  useEffect(() => {
    fetchOSINTData();
  }, []);

  const fetchOSINTData = async () => {
    // Simulating real-time OSINT API call
    setTimeout(() => {
      setAssets([
        { id: 1, name: "Web Server", category: "Hardware", description: "A physical server hosting the company website" },
        { id: 2, name: "Router", category: "Hardware", description: "Network router for managing internet traffic" },
        { id: 3, name: "E-commerce Platform", category: "Software", description: "Web application for online shopping" },
        { id: 4, name: "Content Management System (CMS)", category: "Software", description: "Software to manage and publish content" },
        { id: 5, name: "MySQL Database", category: "Software", description: "Stores transactional and user data" },
        { id: 6, name: "Customer Records", category: "Data", description: "Database of customer data" },
        { id: 7, name: "Transaction Logs", category: "Data", description: "Financial transaction logs" },
        { id: 8, name: "User Credentials", category: "Data", description: "Stored usernames, passwords, tokens" },
        { id: 9, name: "Employee", category: "People", description: "Company employees managing infrastructure" },
        { id: 10, name: "Customer", category: "People", description: "End-users making purchases" },
        { id: 11, name: "Network Administrator", category: "People", description: "IT staff maintaining network security" },
        { id: 12, name: "Payment Processing", category: "Process", description: "Handling online payments securely" },
        { id: 13, name: "Account Authentication", category: "Process", description: "Authentication processes for logins" },
        { id: 14, name: "Backups", category: "Process", description: "Backup systems for disaster recovery" },
      ]);

    setThreats([
        { id: 1, asset_id: 1, name: "DDoS Attack", vulnerability: "Flooding server with requests", risk_score: 16 },
        { id: 2, asset_id: 9, name: "Employee Phishing", vulnerability: "Accidental phishing attacks", risk_score: 15 },
        { id: 3, asset_id: 1, name: "Physical Breach", vulnerability: "Physical break-in to the server room", risk_score: 15 },
        { id: 4, asset_id: 3, name: "SQL Injection", vulnerability: "Malicious SQL code injection", risk_score: 20 },
        { id: 5, asset_id: 8, name: "Weak Passwords", vulnerability: "Insecurely stored credentials", risk_score: 20 },
        { id: 6, asset_id: 12, name: "No Multi-Factor Authentication", vulnerability: "Lack of account authentication (MFA)", risk_score: 15 },
        { id: 7, asset_id: 14, name: "No Backups", vulnerability: "Lack of backups for company systems", risk_score: 15 },
        { id: 8, asset_id: 3, name: "E-commerce Down", vulnerability: "Platform outage causes business losses", risk_score: 12 },
        { id: 9, asset_id: 9, name: "Lack of Training", vulnerability: "Employees making mistakes in IT security", risk_score: 10 },
        { id: 10, asset_id: 12, name: "Payment Platform Down", vulnerability: "Loss of transactions and credibility", risk_score: 12 },
        { id: 11, asset_id: 9, name: "Excessive Privileges", vulnerability: "Employees having too many access rights", risk_score: 16 },
        { id: 12, asset_id: 6, name: "Weak Encryption", vulnerability: "Customer records lacking encryption", risk_score: 15 },
        { id: 13, asset_id: 2, name: "Outdated Firmware", vulnerability: "Old firmware increases router risk", risk_score: 12 },
        { id: 14, asset_id: 4, name: "Website Defacement", vulnerability: "Hacking into CMS and altering content", risk_score: 4 },
        { id: 15, asset_id: 6, name: "Data Leak", vulnerability: "Exposure of sensitive customer data", risk_score: 15 },
        { id: 16, asset_id: 2, name: "Man-in-the-Middle Attack", vulnerability: "Intercepting communications", risk_score: 10 },
      ]);
    }, 1000);
  };

  const filteredThreats = threats
    .filter(threat => threat.risk_score >= riskFilter)
    .sort((a, b) => b.risk_score - a.risk_score);

  return (
    <div className="p-6 bg-gray-100 min-h-screen">
      <h1 className="text-2xl font-bold mb-4">Real-Time Threat Intelligence</h1>
      
      <div className="flex items-center mb-4">
        <label className="mr-2 font-semibold">Filter by Risk Score:</label>
        <input
          type="number"
          value={riskFilter}
          onChange={(e) => setRiskFilter(Number(e.target.value))}
          className="p-1 border rounded"
        />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <AssetList assets={assets} />
        <ThreatList threats={filteredThreats} />
      </div>
    </div>
  );
};
const AssetList = ({ assets }) => (
  <div className="bg-white p-4 shadow rounded-lg">
    <h2 className="text-xl font-semibold mb-2">Asset Inventory</h2>
    <table className="w-full border-collapse border border-gray-300">
      <thead>
        <tr className="bg-gray-200">
          <th className="border p-2">Name</th>
          <th className="border p-2">Category</th>
          <th className="border p-2">Description</th>
        </tr>
      </thead>
      <tbody>
        {assets.length === 0 ? (
          <tr><td colSpan="3" className="text-center p-2">Loading assets...</td></tr>
        ) : (
          assets.map(asset => (
            <tr key={asset.id} className="border-t">
              <td className="border p-2">{asset.name}</td>
              <td className="border p-2">{asset.category}</td>
              <td className="border p-2">{asset.description}</td>
            </tr>
          ))
        )}
      </tbody>
    </table>
  </div>
);

const ThreatList = ({ threats }) => (
  <div className="bg-white p-4 shadow rounded-lg">
    <h2 className="text-xl font-semibold mb-2">Threat Intelligence Overview</h2>
    <table className="w-full border-collapse border border-gray-300">
      <thead>
        <tr className="bg-gray-200">
          <th className="border p-2">Threat</th>
          <th className="border p-2">Vulnerability</th>
          <th className="border p-2">Risk Score</th>
        </tr>
      </thead>
      <tbody>
        {threats.length === 0 ? (
          <tr><td colSpan="3" className="text-center p-2">No threats found...</td></tr>
        ) : (
          threats.map(threat => (
            <tr key={threat.id} className="border-t">
              <td className="border p-2">{threat.name}</td>
              <td className="border p-2">{threat.vulnerability}</td>
              <td className="border p-2">{threat.risk_score}</td>
            </tr>
          ))
        )}
      </tbody>
    </table>
  </div>
);

export default ThreatDashboard;
