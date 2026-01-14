
from core.memory import Memory
from core.state import State
from core.graph.recall import recall
from core.graph.reinforce import reinforce
from core.identity.self import Identity

def add_memory(content):
    state = State()
    mem = Memory(content)
    state.data["memories"][mem.id] = mem.__dict__
    state.data["edges"].setdefault(mem.id, [])
    state.save()
    print("Stored:", mem.id)

def recall_memories(cue=None):
    state = State()
    results = recall(
        state.data["memories"],
        state.data["edges"],
        state.data["identity_bias"],
        cue
    )
    recalled_ids = [mem["id"] for _, mem in results]
    reinforce(state, recalled_ids)
    state.save()
    for score, mem in results:
        print(f"{score:.3f} :: {mem['content']}")
    ident = Identity(state.data["identity_bias"])
    print("Identity:", ident.describe())
