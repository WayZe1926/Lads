def predict(features):

    speed = features[0]

    if speed > 20:
        return 80

    if speed > 10:
        return 40

    return 10