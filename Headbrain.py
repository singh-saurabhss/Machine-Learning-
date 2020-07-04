import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Reading Data
data=pd.read_csv('C:\\Users\\Saurabh singh\\Downloads\\headbrain.csv')
data.head()

#collecting X and Y
x=data['Head Size(cm^3)'].values
y=data['Brain Weight(grams)'].values

#calculating coefficient

#mean x and y
mean_x=np.mean(x)
mean_y=np.mean(y)

#Total number of values
n=len(x)

#using the formula to calculate b1 and b2
numer=0
denom=0
for i in range(n):
    numer+=(x[i]-mean_x)*(y[i]-mean_y)
    denom+=(x[i]-mean_x)**2
b1=numer/denom
b0=mean_y-(b1*mean_x)

#printing coefficient
print("coefficients")
print(b1,b0)

#plotting values and regression line

max_x=np.max(x)+100
min_x=np.min(x)-100

#calculating line values X and Y
x=np.linspace(min_x,max_x,1000)
y=b0+b1*x

#plotting line
plt.plot(x,y,color='#58b970',label='Regression Line')
#plotting scatter points
plt.scatter(x,y,c='#ef5423',label='sactter plot')

plt.xlabel('Head Size in cm^3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()

#calculating root mean squares error
rmse=0
for i in range (n):
    y_pred=b0+b1*x[i]
    rmse+=(y[i]-y_pred)**2
rmse=np.sqrt(rmse/n)
print("RMSE")
print(rmse)

#calculating R2 score
ss_tot=0
ss_res=0
for i in range(n):
    y_pred=b0+b1*x[i]
    ss_tot+=(y[i]-mean_y)**2
    ss_res+=(y[i]-y_pred)**2
r2=1-(ss_res/ss_tot)
print("R2 Score")
print(r2)
    

coefficients
0.26342933948939945 325.57342104944223



RMSE
0.0
R2 Score
1.0

