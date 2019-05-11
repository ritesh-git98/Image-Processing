import numpy as np
import math
import csv
def dist(a,b,i):
    distance=0;
    for x in range(0,8):
        distance += np.square(float(a[i][x]) - float(b[x]));
    return np.sqrt(distance);
        

a=[];
with open('diabetes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    count=0;
    for row in csv_reader:
        count=count+1;
        a.append(row);
b=[];
temp=[];
c=0;
e=0;
k=np.sqrt(count);
print("INPUT\n");
print("Pregnancies:");
b.append(input());
print("\nGlucose:");
b.append(input());
print("\nBloodPressure:");
b.append(input());
print("\nSkinThickness:");
b.append(input());
print("\nInsulin:");
b.append(input());
print("\nBMI:");
b.append(input());
print("\nDiabetesPedigreeFunction:");
b.append(input());
print("\nage:");
b.append(input());
a[0].append("dist");
for i in range(1,count):
  a[i].append(dist(a,b,i));

for i in range(1,count):
    for j in range(i,count-i-1):
        if(a[i][9]>a[j][9]):
            temp=a[i];
            a[i]=a[j];
            a[j]=temp;
  
    
for j in range(int(k)):
    if(a[j+1][8]=='1'):
        c=c+1;
    elif(a[j+1][8]=='0'):
        e=e+1;
print(c,e);
if(c>e):
    print("Outcome is Diabatic");
else:
    print("Outcome is Non-Diabatic");





