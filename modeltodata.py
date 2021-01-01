import sys
from casacore.tables import table

with table(sys.argv[1], readonly=False) as t:
    t.putcol('DATA', t.getcol('MODEL_DATA'))
