import json, datetime

class AuditLogger:
    def log(self, action, filename):
        entry = {
            "time": datetime.datetime.utcnow().isoformat(),
            "action": action,
            "file": filename
        }
        with open("audit.log", "a") as f:
            f.write(json.dumps(entry) + "\n")
