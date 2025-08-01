import pandas as pd 
import matplotlib.pyplot as plt
df=pd.DataFrame({
    'model':['bmw','bens','merc','toyota'],
    'mpg':[21,21,22.8,21.4],
    'cyl':[6,6,4,6],
   'disp':[160,160,108,258],
    'hp':[110,110,93,110],
     'dart':[3.9,3.9,2.9,2.1],
    'wt':[2.6,3.6,2.5,6.2],
     'qsec':[16.46,16.12,16.11,16.47],
    'vc':[1,1,1,1],
    'am':[1,1,1,0],
    'gear':[4,4,3,3],
    'carb':[4,4,4,1]})
   
print(df)