# The "Linguist-Defender" Logic
def translate_alert(tactic_id):
    mapping = {
        "T1190": "An attacker is trying to exploit a hole in our public web software.",
        "T1003.001": "An intruder is attempting to steal passwords directly from the computer's memory.",
        "T1486": "Critical Alert: Files are being locked and held for ransom."
    }
    return mapping.get(tactic_id, "Unknown technical event detected. Investigation required.")

# Example usage for your automation tool
alert_id = "T1003.001"
print(f"COMMUNICATIONS SUMMARY: {translate_alert(alert_id)}")
