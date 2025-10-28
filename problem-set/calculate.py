
rate = 1500 #1500 per day

def gross(days) :
    return days * rate

def deduction() :
    ph = 450
    sss = 750
    gsis = 500
    return ph + sss + gsis
    
def tax(days) :
    g = gross(days)
    return g * 0.10

def net(days) :
    g = gross(days)
    d = deduction()
    t = tax(days)
    return g - d - t