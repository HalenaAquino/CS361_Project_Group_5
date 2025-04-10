
"""
Threat Report Generator Module

This module automates the generation of comprehensive threat intelligence reports in both PDF and CSV formats.
Each report includes a header, the threat details (threat description, risk score, and mitigation plan if available),
and the timestamp of when the report is generated.

Required Library:
    - fpdf (Install via: pip install fpdf)

Usage:
    Run this module directly to generate sample reports:
        - A PDF report saved as "threat_report.pdf"
        - A CSV report saved as "threat_report.csv"
"""

from fpdf import FPDF
import csv
from datetime import datetime

class ThreatReportPDF(FPDF):
    def header(self):
        """Creates the header of the PDF report."""
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Threat Intelligence Report", ln=True, align="C")
        self.ln(10)

    def add_threat(self, threat, score, mitigation=None):
        """
        Adds a threat entry to the PDF report.
        
        Parameters:
            threat (str): Description of the threat.
            score (int or float): Risk score associated with the threat.
            mitigation (str, optional): Mitigation plan if available.
        """
        self.set_font("Arial", "", 12)
        threat_entry = f"Threat: {threat} | Risk Score: {score}"
        self.cell(0, 10, threat_entry, ln=True)
        if mitigation:
            
            self.set_font("Arial", "I", 10)
            self.cell(0, 10, f"Mitigation: {mitigation}", ln=True)
        self.ln(5)

def generate_pdf_report(threats, filename="threat_report.pdf"):
    """
    Generates a PDF report for a list of threats.
    
    Parameters:
        threats (list): A list of threat dictionaries, each with keys "threat", "score", and optionally "mitigation".
        filename (str): The filename for the output PDF report.
    """
    pdf = ThreatReportPDF()
    pdf.add_page()

    
    report_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    pdf.set_font("Arial", "I", 10)
    pdf.cell(0, 10, f"Report generated on: {report_time}", ln=True)
    pdf.ln(5)
    

    for entry in threats:
        threat = entry.get("threat", "Unknown Threat")
        score = entry.get("score", "N/A")
        mitigation = entry.get("mitigation")
        pdf.add_threat(threat, score, mitigation)
    

    pdf.output(filename)
    print(f"PDF report generated: {filename}")


def generate_csv_report(threats, filename="threat_report.csv"):
    """
    Generates a CSV report for a list of threats.
    
    Parameters:
        threats (list): A list of threat dictionaries, each with keys "threat", "score", and optionally "mitigation".
        filename (str): The filename for the output CSV report.
    """
    headers = ["Threat", "Risk Score", "Mitigation", "Timestamp"]
    report_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        for entry in threats:
            writer.writerow({
                "Threat": entry.get("threat", "Unknown Threat"),
                "Risk Score": entry.get("score", "N/A"),
                "Mitigation": entry.get("mitigation", ""),
                "Timestamp": report_time
            })
    print(f"CSV report generated: {filename}")


if __name__ == "__main__":
   
    sample_threats = [
        {
            "threat": "SQL Injection",
            "score": 25,
            "mitigation": "Use parameterized queries and perform input validation."
        },
        {
            "threat": "Cross-Site Scripting (XSS)",
            "score": 20,
            "mitigation": "Sanitize user inputs and implement Content Security Policy."
        },
        {
            "threat": "DDoS Attack",
            "score": 30,
            "mitigation": "Apply rate limiting and deploy network traffic filtering."
        }
    ]
    generate_pdf_report(sample_threats)
    generate_csv_report(sample_threats)
