import time
from collections import defaultdict

requests = defaultdict(list)

def rps(ip):
    now = time.time()

    requests[ip].append(now)
    requests[ip] = [t for t in requests[ip] if now - t < 10]

    return len(requests[ip])