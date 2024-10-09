from mod.testing import *
import unittest

#tu codigo aquí
def greater_imperativa(a, b):
    if a > b:
        return a
    else:
        return b
    
test_greater(greater_imperativa)
