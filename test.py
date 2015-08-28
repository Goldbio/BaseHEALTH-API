from lib.BaseHealth import *
import sys


key = 'your key'
bh = API(key)

disease= bh.getCuratedContent( sys.argv[1] )

for i in disease:
	print i , disease[i]
#print bh.getAllDiseases()

