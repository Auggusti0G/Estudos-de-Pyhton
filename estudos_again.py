
def maior(a,b,c):
    if a >= b and b >= c:
        return a 
    elif b >= a and b >= c:
        return b
    else:
        return c
resultado = maior(12,232,121212)
print("O maior valor digitado sera :", resultado)