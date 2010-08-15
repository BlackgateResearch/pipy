'''
Viète's formula for calculating π

This Python version copyright
Tristram Oaten, Blackgate Research
<tris@blackgateresearch.com>
'''

from math import sqrt

var = sqrt(2)
caret = sqrt(2) / 2

for i in range(18):
   var = sqrt(2 + var)
   caret = caret * (var / 2)

print 2 / caret
