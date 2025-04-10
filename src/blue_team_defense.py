
"""
Advanced Blue Teaming Defensive Script

This script implements an automated defensive mechanism that blocks malicious IP addresses.
It adds a rule to the system firewall (iptables) to drop all incoming traffic from a specified IP.

Usage:
    python blue_team_defense.py <IP_ADDRESS>

Note:
    - Ensure that iptables is installed and accessible.
    - Run the script with sufficient privileges (e.g., as root) to modify firewall rules.
"""

import os
import sys

def block_ip(ip):
    """
    Blocks the specified IP address using iptables.

    Parameters:
        ip (str): The IP address to be blocked.
        
    Returns:
        bool: True if the command executed successfully, False otherwise.
    """
    command = f"iptables -A INPUT -s {ip} -j DROP"
    print(f"Executing: {command}")
    result = os.system(command)
    if result == 0:
        print(f"Successfully blocked IP: {ip}")
        return True
    else:
        print(f"Error: Failed to block IP: {ip}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python blue_team_defense.py <IP_ADDRESS>")
        sys.exit(1)
    
    ip_address = sys.argv[1]
    block_ip(ip_address)

if __name__ == '__main__':
    main()
