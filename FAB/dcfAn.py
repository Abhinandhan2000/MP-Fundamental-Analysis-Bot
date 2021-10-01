import pandas as pd 
import numpy as np 
import math
import csv

data = pd.read_csv("WACC.csv");

data.set_index("Symbol",inplace=True);

print(data);

user = input("Enter company name to search : ");

result = data.loc[user];
#print(result);


r = result.iloc[0:5];
result_to_rows = r.tolist();

print("\n");
print(result_to_rows);
print("\n");

wacc=(result_to_rows[1]/(result_to_rows[1]+result_to_rows[3]))*result_to_rows[0]+(result_to_rows[3]/(result_to_rows[1]+result_to_rows[3]))*result_to_rows[2]*(1-(result_to_rows[4]/100));
print("%.2f" % wacc);


write_data = data["WACC"][user:user].fillna(wacc,inplace=True);

print(data.head());

data.to_csv("WACC.csv");

d1 = result.iloc[11:16];
d2 = result.iloc[16:17];

ufcf = d1.tolist();
result_d2 = d2.tolist();
print(ufcf);
print(result_d2);

tv = result_d2;
tv = (ufcf[4]/((1+(wacc/100))**(4+1)))
nfv = 0;
dcf=[];
npv=0;
for i in range (len(ufcf)):
	nfv += ufcf[i];

for i in range (len(ufcf)):
	dcf.append(ufcf[i]/((1+(wacc/100))**(i+1)))
for i in range (len(ufcf)):
	npv+=dcf[i]
npv += tv;
print('\n---------------------------------------------------------------\n');
for i in range (len(ufcf)):
	print("202{} year -> {}".format(i+1,ufcf[i]));
print(nfv);
for i in range (len(dcf)):
	print("202{} year -> {}".format(i+1,dcf[i]));
print(npv);	

if((npv - nfv) > 0):
	print("The investment is profitable. The profit is estimated to be in %.2f" %(npv - nfv) , "(cr)");
elif((npv - nfv) == 0):
	print("The investment results in neither gain or los");
else:
	print("The investment is non-profitable!");		