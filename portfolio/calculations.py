def total_pl(current, avg, shares):
    return (current - avg) * shares

def percent_pl(current, avg):
    return ((current - avg) / avg) * 100