import time
import uuid

class Epoch:
    def __init__(self, name, tone=None):
        self.id = f"epoch_{uuid.uuid4().hex[:8]}"
        self.name = name
        self.tone = tone
        self.started_at = int(time.time())
        self.ended_at = None
        self.anchor_memories = []

    def close(self):
        self.ended_at = int(time.time())

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "tone": self.tone,
            "started_at": self.started_at,
            "ended_at": self.ended_at,
            "anchor_memories": self.anchor_memories
        }