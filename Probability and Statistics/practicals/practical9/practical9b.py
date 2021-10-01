import random
import matplotlib.pyplot as plt
import statistics

xdata = []
ydata = []

for i in range(int(input("Enter the number of elements you  want: "))):
    xdata.append(random.randint(1, 200))
    ydata.append(random.randint(1, 200))

xdata.sort()
ydata.sort()

n = len(xdata)

yacc = sum(ydata)  # Σy
xacc = sum(xdata)  # Σx

xaccyacc = sum([i * j for i, j in zip(xdata, ydata)])  # Σxy
xacc2 = sum([i * i for i in xdata])  # Σx^2
yacc2 = sum([i * i for i in ydata])  # Σy^2

intercept = (yacc * xacc2 - xacc * xaccyacc) / (xacc2 - xacc ** 2)

slope = (n * xaccyacc - xacc * yacc) / (n * xacc2 - xacc ** 2)

xval = list(range(200))  # list of x values
yval = [intercept + slope * i for i in xval]  # list of y values predicted on x

# multiple linear regression with 2 independent variables.
"""Multiple linear regression: Y=a+b1X1+b2X2+b3X3+..bKcK+e
   intercept=mean(Y)-b1*mean(X)-b2*mean(X2)
   b1=(Σx2^2)(Σx1y)-(Σx1x2)(Σx2y)/(Σx1^2)(Σx2^2)-(Σx1x2)^2
   b2=(Σx1^2)(Σx2y)-(Σx1x2)(Σx1y)/(Σx1^2)(Σx2^2)-(Σx1x2)^2
"""
xmuldata1 = []  # X1 data
xmuldata2 = []  # X2 data
ymuldata = []  # Y data

for i in range(20):
    xmuldata1.append(random.randint(1, 200))
    xmuldata2.append(random.randint(1, 200))
    ymuldata.append(random.randint(1, 200))

xmulacc2square = sum([i * i for i in xmuldata2])  # (Σx2^2)
xmulacc1ymulacc = sum([i * j for i, j in zip(xmuldata1, ydata)])  # (Σx1y)

xmulacc1xmulacc2 = sum([i * j for i, j in zip(xmuldata1, xmuldata2)])  # (Σx1x2)

xmulacc2ymulacc = sum([i * j for i, j in zip(xmuldata2, ydata)])  # (Σx2y)
xmulacc1square = sum([i * i for i in xmuldata1])  # (Σx1^2

b1 = ((xmulacc2square * xmulacc1ymulacc) - (xmulacc1xmulacc2 * xmulacc2ymulacc)) / (
            (xmulacc1square * xmulacc2square) - (xmulacc1xmulacc2) ** 2)
b2 = ((xmulacc1square * xmulacc2ymulacc) - (xmulacc1xmulacc2 * xmulacc1ymulacc)) / (
            (xmulacc1square * xmulacc2square) - (xmulacc1xmulacc2) ** 2)

a = statistics.mean(ymuldata) - b1 * (statistics.mean(xmuldata1)) - b2 * (statistics.mean(xmuldata2))

xmulval1 = list(range(200))  # list of x1 values
xmulval2 = list(range(200))  # list of x2 values
ymulval = [a + b1 * i + b2 * j for i, j in zip(xmulval1, xmulval2)]  # list of y values predicted on x1 and x2 values.
print(xmulval1)
print(xmulval2)
print(ymulval)
# scatter plot
plt.scatter(xmuldata1, ymuldata, color="red")
plt.scatter(xmuldata2, ymuldata, color="green")
plt.plot(xmulval1, xmulval2, ymulval, color="red")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Multiple linear Regression")
plt.show()