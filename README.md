# Security Automator Tool

## How to Run the Application

1. Open Codespace (Github) or any terminal and type this:
         
         bash demo.sh
         
2. Or try the manual executable way (optional):
   Open Codespace (Github) or any terminal and type this:
         
         chmod +x demo.sh
         
   Press enter.
   Then type:
         
         ./demo.sh

**This tool reduces manual analysis time for SOC analysts.**

Here’s a quick rundown of what this Security Automation Tool / script is doing and what its output will look like:
What it does
IP Validation
Uses a precise regex to validate IPv4 addresses (0.0.0.0 → 255.255.255.255).
Invalid formats (like 999.999.999.999 or not_an_ip) get flagged.
Incident Staging
For valid IPs, it creates a JSON-like log entry with:
Timestamp (UTC ISO format)
Target IP
Severity (HIGH by default)
Action (STAGED_FOR_BLOCK)
Return
Returns a dictionary indicating success (SUCCESS) or error (ERROR).
Test Suite
Runs four sample IPs through stage_incident to verify logic without user input.

Sample Output
🔍 RUNNING AUTOMATED LOGIC TEST...
========================================
[SUCCESS] Testing 8.8.8.8: {'timestamp': '2026-03-18T21:50:12.345678Z', 'target_ip': '8.8.8.8', 'severity': 'HIGH', 'action': 'STAGED_FOR_BLOCK'}
[ERROR] Testing 999.999.999.999: Invalid IP format: 999.999.999.999
[SUCCESS] Testing 10.0.0.1: {'timestamp': '2026-03-18T21:50:12.345789Z', 'target_ip': '10.0.0.1', 'severity': 'HIGH', 'action': 'STAGED_FOR_BLOCK'}
[ERROR] Testing not_an_ip: Invalid IP format: not_an_ip

✅ Highlights
Clean separation of validation, staging, and logging.
Handles errors gracefully without crashing.
Ready for integration into a larger SOC automation workflow.
