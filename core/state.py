
import json, os

STATE_VERSION = "0.3.0"

class State:
    def __init__(self, path="state.json"):
        self.path = path
        self.data = {
            "version": STATE_VERSION,
            "memories": {},
            "edges": {},
            "identity_bias": {}
        }
        if os.path.exists(path):
            self.load()

    def load(self):
        with open(self.path, "r") as f:
            self.data = json.load(f)

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=2)
