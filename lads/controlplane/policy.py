def decision(score):

    if score > 150:
        return "BLOCK"

    if score > 100:
        return "CHALLENGE"

    return "ALLOW"