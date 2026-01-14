
import base64, random

def scatter(data):
    shards = [data[i:i+8] for i in range(0, len(data), 8)]
    random.shuffle(shards)
    return shards

def gather(shards):
    return ''.join(sorted(shards))

def encrypt(data):
    return base64.b64encode(data.encode()).decode()

def decrypt(data):
    return base64.b64decode(data.encode()).decode()
