import time

def record_trace(state, query, memories, bias, epoch=None):
    trace = {
        "timestamp": int(time.time()),
        "query": query,
        "memories_returned": memories,
        "identity_bias": bias,
        "epoch_context": epoch
    }
    state.setdefault("witness_log", []).append(trace)
    return trace