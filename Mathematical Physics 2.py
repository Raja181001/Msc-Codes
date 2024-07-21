from pandas import *
from numpy import *

data =[['1.','Alpha','50','40',''],
       ['2.', 'Beta', '60','39',''],
       ['3.', 'Gamma', '20','80',''],
       ['4.', 'Delta', '80','20',''],
       ['5.', 'Charlie', '70','60',''],
       ['6.', 'Ram', '39','60',''],
       ['7.', 'Shayam', '65','75',''],
       ['8.', 'Raju', '69','90',''],
       ['9.', 'Babu Baiya', '56','69',''],
       ['10.', 'aradhna', '90','56',''],
       ]
headers = ['Sr.no','Name','Subject 1','subject 2','Total']

df = DataFrame(data , columns=headers)
print()
print('Input Table')
print(df.to_markdown(index=False))

d = 0
while d < len(data):
       data[d][4] = int(data[d][3]) + int(data[d][2])
       d+=1

for i in range(len(data)-1,0,-1):
       for j in range(i):
              if  data[j][4] < data[j+1][4]:
                     temp = data[j]
                     data[j] = data[j+1]
                     data[j+1] = temp

df1 = DataFrame(data,columns=headers)
print()
print('Output table descending Order')
print(df1.to_markdown(index=False))
print()
print()
