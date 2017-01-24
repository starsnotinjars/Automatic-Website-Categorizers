import re
from shutil import copyfile
import fileinput

upperlimit=7000
lowerlimit=5000
delta=50

diff=upperlimit-lowerlimit

a=int(float(diff)/float(delta))
# a=2
for i in range(1,a+1):

	replacements = {"for a in range(5000,5050):":"for a in range("+str(5000+(delta*i))+","+str(5050+(delta*i))+"):"}

	with open('descriptions4.py') as infile, open("descriptions"+str(4+i)+".py", 'w') as outfile:
    		for line in infile:
       			for src, target in replacements.iteritems():
            			line = line.replace(src, target)
        		outfile.write(line)

#	copyfile("descriptions3.py", "descriptions"+str(i)+".py")

#        		print(line.replace("for a in range(3263,3363):", "for a in range("+str(3263+(a*i))+","+str(3363+(a*i))+"):"), end='')



#"for a in range("+str(3263+(a*i))"+","+str(3363+(a*i))+"):"

#"for a in range("+str(3263+(delta*i))+","+str(3363+(delta*i))+"):"


