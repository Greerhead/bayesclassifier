import numpy as np
from scipy.stats import multivariate_normal
import sys

f = open(sys.argv[1])
Setosa = np.genfromtxt(f, delimiter = ",", skip_header =1, skip_footer = 133, usecols=(0,1,2,3), dtype = float)
f.close()
f = open(sys.argv[1])
Versicolor = np.genfromtxt(f, delimiter = ",", skip_header =53, skip_footer = 81, usecols=(0,1,2,3), dtype = float)
f.close()
f = open(sys.argv[1])
Virginica = np.genfromtxt(f, delimiter = ",", skip_header = 105, skip_footer = 29, usecols = (0,1,2,3), dtype = float)
print Setosa
print Versicolor
print Virginica
f.close()

f = open(sys.argv[1])
setosaMean = np.genfromtxt(f, delimiter = ",", skip_header = 176, skip_footer = 10, dtype = float)
print setosaMean
f.close()
f = open(sys.argv[1])
versicolorMean = np.genfromtxt(f, delimiter = ",", skip_header = 178, skip_footer = 8, dtype = float)
print versicolorMean
f.close()
f = open(sys.argv[1])
virginicaMean = np.genfromtxt(f, delimiter = ",", skip_header = 180, skip_footer = 6, dtype = float)
print virginicaMean
f.close()

f = open(sys.argv[1])
setosaCov = np.genfromtxt(f, skip_header = 157, skip_footer = 23, dtype = float, usecols=(0,1,2,3),  delimiter = ',')
for i in range(0,4):
	for j in range(0,4):
		if i != j:
			setosaCov[i,j] =0
print setosaCov

f.close()
f = open(sys.argv[1])
versiCov = np.genfromtxt(f,skip_header = 163, skip_footer =18, dtype = float, usecols=(0,1,2,3), delimiter = ',')
for i in range(0,4):
	for j in range(0,4):
		if i != j:
			versiCov[i,j] =0
print versiCov
f.close()
f = open(sys.argv[1])
virCov = np.genfromtxt(f,skip_header = 169, skip_footer =13, dtype = float, usecols=(0,1,2,3), delimiter = ',')
for i in range(0,4):
	for j in range(0,4):
		if i != j:
			virCov[i,j] =0
f.close()
print virCov
f = open(sys.argv[1])
setPrev = np.genfromtxt(f, skip_header = 182, skip_footer = 4, dtype = float)
f.close()
f = open(sys.argv[1])
versiPrev = np.genfromtxt(f, skip_header = 184, skip_footer = 2, dtype = float)
f.close()
f = open(sys.argv[1])
virPrev = np.genfromtxt(f, skip_header = 186, skip_footer = 0, dtype = float)
f.close()
print setPrev
print versiPrev
print virPrev

f = open(sys.argv[2])
test = np.genfromtxt(f, delimiter = ',', dtype = float, usecols = (0,1,2,3))
f.close()
f = open(sys.argv[2])
realLabel = np.genfromtxt(f, delimiter = ',', dtype = str, usecols = (4))
f.close()
predictedLabel = []
print test
for i in range(0,150):
	norm1 = multivariate_normal.pdf(test[i], setosaMean, setosaCov)* .33
	norm2 = multivariate_normal.pdf(test[i], versicolorMean, versiCov) * .33
	norm3 = multivariate_normal.pdf(test[i], virginicaMean, virCov)*.33
	Norms = [norm1,norm2,norm3]
	
	max = np.amax(Norms)
	if max == Norms[0]:
		print "Iris-setosa"
		predictedLabel.append("Iris-setosa")	
	elif max == Norms[1]:
		print "Iris-versicolor"
		predictedLabel.append("Iris-versicolor")
	elif max == Norms[2]:
		print "Iris-virginica"
		predictedLabel.append("Iris-virginica")

print '\n'
print predictedLabel
print '\n'
print realLabel

print predictedLabel[0] == realLabel[0]
confusion =[]
for i in range (0,150):
	print predictedLabel[i] == realLabel[i]
	confusion.append(realLabel[i] ==realLabel[i])
print setosaCov

	

	
