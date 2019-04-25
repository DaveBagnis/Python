def somma(a,b):
    return a+b

def moltip(a,b):
    return a*b

def somma_molt(a,b):
    return a+b, a*b

def molt_somma(a,b):
    return a*b, a+b

print("Somma = " + str(somma(2,7)))
print("Moltiplicazione = " + str(moltip(2,7)))
print("Somma e moltiplicazione = " + str(somma_molt(2,7)))
print("Moltiplicazione e somma = " + str(molt_somma(2,7)))