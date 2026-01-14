
class Identity:
    def __init__(self, bias):
        self.bias = bias

    def describe(self):
        dominant = sorted(self.bias.items(), key=lambda x: x[1], reverse=True)
        if not dominant:
            return "Akasha has no preferences yet."
        return f"Akasha is drawn toward memory {dominant[0][0][:8]}"
