'''solucion'''

def sma(*args):
    rtd = 0
    for arg in args:
            rtd += arg
    return rtd
print(sma(7, 7, 5, 8))