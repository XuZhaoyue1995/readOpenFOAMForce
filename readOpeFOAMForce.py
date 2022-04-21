import os
fileDir='../../rankine01Ave'
postDir='/postProcessing/Forces/0/'
fileName='force.dat'
os.chdir(fileDir+postDir)
f1=open(fileName)
f2=open('test.dat','w')
for line in f1:
	if(line[0]!='#'):
		lineS=line.split('(')
		totalX=lineS[1].split(' ')
		pressX=lineS[2].split(' ')
		stressX=lineS[3].split(' ')
		f2.write(lineS[0]+' '+totalX[0]+' '+pressX[0]+' '+stressX[0]+'\n')