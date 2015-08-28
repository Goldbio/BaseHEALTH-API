from lib.BaseHealth import *
import sys


key = '3e364c9f0bf8e2d9a4e69e2d980f23db'
bh = API(key)

disease= bh.getCuratedContent( sys.argv[1] )

for i in disease:
	print i , disease[i]
#print bh.getAllDiseases()

