'''SUbClases: Monitor, raton, teclado'''

from obj import *
from lab import pc

def ordn (obja, objb, objc, objd):
    if isinstance(obja, pc) and isinstance(objb, mn) and isinstance(objc, tcl) and isinstance(objd, ms):
        d = [obja, objb, objc, objd]
        print(d)
obja = pc('hp','on', 'blue', 'rr')
objc = ms('sad')
objd = tcl('hungry')

ordn(obja, objb, objc, objd)

