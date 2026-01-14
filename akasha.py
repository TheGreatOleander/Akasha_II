
from interfaces.cli import add_memory, recall_memories
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Akasha online. Commands: add | recall")
    elif sys.argv[1] == "add":
        add_memory(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "recall":
        cue = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else None
        recall_memories(cue)
