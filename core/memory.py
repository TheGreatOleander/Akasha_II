
import time, hashlib, math

class Memory:
    def __init__(self, content, weight=1.0, tags=None):
        self.timestamp = time.time()
        self.content = content
        self.weight = weight
        self.tags = tags or []
        self.id = hashlib.sha256(
            f"{self.timestamp}:{content}".encode()
        ).hexdigest()

    def decay(self, half_life=3600):
        age = time.time() - self.timestamp
        self.weight *= math.exp(-age / half_life)
