
import os
from qual2db.manager import Manager

try:
    os.remove('sample.db')
except:
    pass

m = Manager('sample.db')
m.listSurveys()
s = m.add_survey('SV_03xFTFmDEiceCP3')
