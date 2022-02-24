import pandas as pd 
import numpy as np 
import math


data = pd.read_csv("VolatileIndexData.csv");

data.set_index("Symbol",inplace=True);

#print(data);

#user = input("Enter company name to search : ");
#print(user)
#print("Above printes user values")
# Algorithm to sort , extract and list the row values to a variable container
result = data.loc['AXISBANK'];
print(result);

r = result.iloc[:];
l = r.tolist();

print("\n");
print(l);
print("\n");

# Formula to calculate volatile index
s=[];
avg=sum(l)/len(l);

for i in range(len(l)):
	s.append((avg-l[i])*(avg-l[i]))

res=math.sqrt(sum(s)/len(s));
print("The volatility is %.2f" % avg + " ± %.2f" % res);