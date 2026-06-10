METRICS = {
    "requests": 0,
    "blocked": 0,
    "challenged": 0
}

def inc(key):
    METRICS[key] += 1