
def reinforce(state, recalled_ids):
    for mid in recalled_ids:
        state.data["identity_bias"][mid] = (
            state.data["identity_bias"].get(mid, 0.0) + 0.1
        )
    for a in recalled_ids:
        for b in recalled_ids:
            if a == b:
                continue
            state.data["edges"].setdefault(a, [])
            if b not in state.data["edges"][a]:
                state.data["edges"][a].append(b)
