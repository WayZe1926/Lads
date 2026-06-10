from edge.ratelimit import rps
from ml.anomaly import predict

def analyze_request(data):

    ip = data["ip"]

    speed = rps(ip)
    ml = predict([speed])

    score = (speed * 5) + ml

    if score > 150:
        return {"action": "BLOCK", "score": score}

    if score > 100:
        return {"action": "CHALLENGE", "score": score}

    return {"action": "ALLOW", "score": score}