import numpy as np
import sys
f = sys.argv[1]

data = np.genfromtxt(f, delimiter = ",",  usecols = (0,1,2,3))

label = np.genfromtxt(f, dtype = str ,delimiter = ",", usecols = (4))


print data[0]
print label[0]


setosa = []
vcolor = []
virg = []

setosaCov =[]
vColorCov =[]
virgCov = []
for i in range (0,150):
	for j in range (0,4):
		if label[i] == "Iris-setosa":
			setosa.append(data[i,j])
		elif label[i] == "Iris-versicolor":
			vcolor.append(data[i,j])
		elif label[i] == "Iris-virginica":
			virg.append(data[i,j])

for i in range (0,150):
	if label[i] == "Iris-setosa":
		setosaCov.append(data[i])
	elif label[i] == "Iris-versicolor":
		vColorCov.append(data[i])
	elif label[i] == "Iris-virginica":
		virgCov.append(data[i])
Scov = np.cov(setosaCov, rowvar = False)
Colcov = np.cov(vColorCov, rowvar = False)
Vcov = np.cov(virgCov, rowvar = False)

SetRe = np.reshape(setosa,(50,4))
ColRe = np.reshape(vcolor, (50,4))
VirgRe = np.reshape(virg,(50,4))

sPrior = 50.00/150.00
colPrior = 50.00/150.00
vPrior =  50.00/150.00

Smean = np.mean(SetRe, axis =0)
Colmean = np.mean(ColRe, axis =0)
Vmean = np.mean(VirgRe, axis = 0)

output = open(sys.argv[2], "w")
output.write(str("Setosa"))
output.write("\n")
for i in range(0,50):
	for j in range(0,4):
		if j !=3:
			output.write(str(setosa[i+j]))
			output.write(',')
		elif j ==3:
			output.write(str(setosa[i+j]))
			output.write('\n')

output.write("\n")

output.write(str('Versicolor'))
output.write('\n')
for i in range(0,50):
	for j in range(0,4):
		if j !=3:
			output.write(str(vcolor[i+j]))
			output.write(',')
		elif j ==3:
			output.write(str(vcolor[i+j]))
			output.write('\n')
output.write('\n')

output.write(str('Virginica'))
output.write('\n')
for i in range(0,50):
	for j in range(0,4):
		if j !=3:
			output.write(str(virg[i+j]))
			output.write(',')
		elif j ==3:
			output.write(str(virg[i+j]))
			output.write('\n')
output.write('\n')
output.write('Covariance')
output.write('Setosa')
output.write('\n')
for i in range(0,4):
	for j in range(0,4):
		if j != 3:
			output.write(str(Scov[i,j]))
			output.write(',')
		elif j ==3:	
			output.write(str(Scov[i,j]))
			output.write('\n')
output.write('\n')
output.write('Versicolor')
output.write('\n')
for i in range(0,4):
	for j in range(0,4):
		if j != 3:
			output.write(str(Colcov[i,j]))
			output.write(',')
		elif j ==3:	
			output.write(str(Colcov[i,j]))
			output.write('\n')
output.write('\n')
output.write('Virginica')
output.write('\n')
for i in range(0,4):
	for j in range(0,4):
		if j != 3:
			output.write(str(Vcov[i,j]))
			output.write(',')
		elif j ==3:	
			output.write(str(Vcov[i,j]))
			output.write('\n')
output.write('\n')

output.write('Mean')
output.write('\n')
output.write('Setosa ')
output.write('\n')
for i in range(0,4):
		if i != 3:
			output.write(str(Smean[i]))
			output.write(',')
		elif i ==3:	
			output.write(str(Smean[i]))	
output.write('\n')
output.write('versicolor ')
output.write('\n')
for i in range(0,4):
		if i != 3:
			output.write(str(Colmean[i]))
			output.write(',')
		elif i ==3:	
			output.write(str(Colmean[i]))	
output.write('\n')
output.write('Virginica ')
output.write('\n')
for i in range(0,4):
		if i != 3:
			output.write(str(Vmean[i]))
			output.write(',')
		elif i ==3:	
			output.write(str(Vmean[i]))	
output.write('\n')
output.write('sPrior ')
output.write('\n')
output.write(str(sPrior))
output.write('\n')
output.write('colPrior ')
output.write('\n')
output.write(str(colPrior))
output.write('\n')
output.write('vPrior ')
output.write('\n')
output.write(str(vPrior))

output.close()



