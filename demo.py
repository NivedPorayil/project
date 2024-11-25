import pandas as np
import pandas as pd

df1=pd.read_csv("C:/Users/HP/Documents/Mysql/student.unknown",sep=',',header=None)
df1.columns=['name','roll']
print(df1)
df1.to_csv('C:/Users/HP/OneDrive/Documents/student.csv',index=False)
# df2=pd.read_csv("C:/Users/HP/Documents/Mysql/results.unknown",sep=',',header=None)
# df2.columns=['roll','res']
# print(df2)
# df2.to_csv('C:/Users/HP/OneDrive/Documents/result.csv',index=False)