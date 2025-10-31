import json
from pathlib import Path

DATA_FILE = Path("data/user_knowledge.json")

def load_memories():
    """Load memories from a JSON file."""
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def store_memory(text, intent):
    """Store a new memory in the JSON file."""
    memories = load_memories()
    memories.append({"text": text, "intent": intent})
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(memories, f, indent=2)
