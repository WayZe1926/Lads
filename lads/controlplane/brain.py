GLOBAL_DB = {}

def update_reputation(ip, score):

    GLOBAL_DB[ip] = max(0, 100 - score)