def verify_identity(data):

    trust = 0

    if data.get("token") != "valid":
        trust += 50

    if data.get("device_risk", 0) > 60:
        trust += 30

    if trust > 70:
        return "DENY"

    return "ALLOW"