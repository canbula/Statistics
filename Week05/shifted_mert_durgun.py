import central_tendency

def shifted(data):
    return abs((central_tendency.mean(data) - central_tendency.median(data)) / central_tendency.mean(data)) * 100
