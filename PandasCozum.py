import pandas as pd
import numpy as np
sutun = ["Job","O1","O2","O3","O4","O5","PROC","SETUP"]
data =  pd.read_csv(r"E:\Projelerim\single_machine_scheduling\DENEME CSV SETLER\DENEME CSV SETLER\I=5, J=10\Experiment35.csv",delimiter=";")

sutun.append("SUM")
df = pd.DataFrame(columns=sutun)
df.Job = data.Job
df.SETUP = data.SETUP
df.PROC=data.PROC
df.iloc[:,1:6] = data.iloc[:,2:7]
for i in range(1,11):
    dr =  (data.iloc[i-1,2:7].sum()*data.iloc[i-1,7])+data.iloc[i-1,8]
    df.SUM.iloc[[i-1]] = dr

for i in range(1,6):
    df["O"+str(i)]=df["O"+str(i)]*df["PROC"]
dfO = df.sort_values(by="SUM",ascending=1).reset_index(drop=True)
print(dfO)
df1 = dfO.iloc[0,1].tolist()
# df1 = dfO.loc[0]
print(df1)



