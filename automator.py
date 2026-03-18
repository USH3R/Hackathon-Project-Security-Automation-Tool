import datetime
import re

class IPOrchestrator:
    def __init__(self, storage_file="master_blacklist.txt"):
        self.storage_file = storage_file

    def validate_ip(self, ip):
        """Regex to ensure the input is a valid IPv4 address."""
        pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
        return re.match(pattern, ip) is not None

    def prepare_for_blacklist(self, ip, threat_type="Unspecified"):
        """Formats and logs the IP with a high-fidelity timestamp."""
        if not self.validate_ip(ip):
            return f"Error: {ip} is not a valid IPv4 address."
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] | IP: {ip} | THREAT: {threat_type} | STATUS: PENDING_BLOCK\n"
        
        try:
            with open(self.storage_file, "a") as f:
                f.write(entry)
            return f"Successfully staged {ip} for blacklisting."
        except Exception as e:
            return f"Failed to write to storage: {e}"

# --- Execution ---
if __name__ == "__main__":
    bot = IPOrchestrator()
    print("--- Security Automation: IP Staging Tool ---")
    user_ip = input("Enter suspicious IP address: ")
    user_threat = input("Enter threat category (e.g., Brute Force, Phishing): ")
    
    result = bot.prepare_for_blacklist(user_ip, user_threat)
    print(result)
