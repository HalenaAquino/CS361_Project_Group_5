import React, { useState, useEffect } from 'react';
import { Card, CardContent } from "@/components/ui/card";
import { Select, SelectItem } from "@/components/ui/select";
import { Line } from 'react-chartjs-2';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

const Dashboard = () => {
    const [filter, setFilter] = useState('all');
    const [riskData, setRiskData] = useState({
        labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
        datasets: [
            {
                label: 'Risk Score Trend',
                data: [10, 25, 35, 50],
                borderColor: 'red',
                fill: false,
            }
        ]
    });

    useEffect(() => {
        // Simulate fetching real-time data
        const interval = setInterval(() => {
            setRiskData(prevData => {
                const newData = [...prevData.datasets[0].data, Math.floor(Math.random() * 100)];
                return {
                    labels: [...prevData.labels, `Week ${prevData.labels.length + 1}`],
                    datasets: [{
                        ...prevData.datasets[0],
                        data: newData.slice(-4)
                    }]
                };
            });
        }, 5000);

        return () => clearInterval(interval);
    }, []);

    return (
        <div className="p-6 space-y-6">
            <h2 className="text-xl font-bold">Threat Intelligence Dashboard</h2>
            <Card>
                <CardContent>
                    <div className="mb-4">
                        <Select onValueChange={setFilter} defaultValue="all">
                            <SelectItem value="all">All Threats</SelectItem>
                            <SelectItem value="high">High Severity</SelectItem>
                            <SelectItem value="medium">Medium Severity</SelectItem>
                            <SelectItem value="low">Low Severity</SelectItem>
                        </Select>
                    </div>
                    <Line data={riskData} />
                </CardContent>
            </Card>
        </div>
    );
};

export default Dashboard;
