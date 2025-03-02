import React from "react";

const ThreatDashboard = () => {
  return (
    <div className="p-6 bg-gray-100 min-h-screen">
      <h1 className="text-2xl font-bold mb-4">Real-Time Threat Intelligence</h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white p-4 shadow rounded-lg">
          <h2 className="text-xl font-semibold mb-2">Threat Logs</h2>
          <p>Live Threat Logs will be displayed here.</p>
        </div>

        <div className="bg-white p-4 shadow rounded-lg">
          <h2 className="text-xl font-semibold mb-2">Risk Scores</h2>
          <p>Current risk assessments will appear here.</p>
        </div>

        <div className="bg-white p-4 shadow rounded-lg">
          <h2 className="text-xl font-semibold mb-2">Real-Time Alerts</h2>
          <p>Immediate threat alerts will be shown here.</p>
        </div>
      </div>
    </div>
  );
};

export default ThreatDashboard;

