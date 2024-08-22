import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge

curDir = os.getcwd()
os.chdir(curDir)

dataSet = pd.read_csv('data.txt')
x = dataSet.iloc[: ,:-1].values
y = dataSet.iloc[: , -1].values

l=10
ridge = Ridge(alpha=l)
ridge.fit(x, y)
ridge_coeff = ridge.coef_
ridge_intercept = ridge.intercept_

xTest = [1, 2, 3, 4]
yPred = ridge.predict(pd.DataFrame(xTest))

plt.figure(figsize=(12,6) , dpi = 90)
plt.plot(xTest, yPred , c ='r' , linewidth = 2)
plt.scatter(x, y)
plt.ylim(ymin = 0 , ymax = 9)
plt.xlim(xmin = 0 , xmax = 7)

plt.text(xTest[-1], yPred[-1], ' y = '   +    str('%.2f' %ridge_coeff)  + ' * X +'  +  str('%.2f' %ridge_intercept)    
                                                   +  '  For \u03BB or  \u03b1 = ' +    str(l)  ,   fontsize = 12)
plt.title('ridge Regression')
plt.show()