
def recall(memories, edges, bias, cue=None, top_k=3):
    scored = []
    for mid, mem in memories.items():
        score = mem.get("weight", 1.0)
        score += bias.get(mid, 0.0)
        if cue and cue.lower() in mem.get("content","").lower():
            score *= 2.0
        score += len(edges.get(mid, [])) * 0.2
        scored.append((score, mem))
    scored.sort(reverse=True, key=lambda x: x[0])
    return scored[:top_k]
