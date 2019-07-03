import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xgboost as xgb

train = pd.read_csv('train.csv')  


labels=train.iloc[:,0].values

from sklearn.preprocessing import MinMaxScaler  
scaler = MinMaxScaler(feature_range = (0, 1))
features= scaler.fit_transform(train.iloc[:,1:])  

gbm = xgb.XGBClassifier(max_depth=3, n_estimators=300, learning_rate=0.05).fit(features, labels)


import pickle

xg="gbm.pkl"
with open(xg,'wb') as file:
    pickle.dump(gbm,file)


ls=[614689,400,5729,199.618296223,67.8124694734,9.36619224194,0.359533601106,4.09448755266,669,39.1937406855,2565.61251863,1404323,563,20057,967.720641729,579.431127684,4.47379849183,0.805680232136,6.24180594033,4027,57.6438389197,3201.29370629]    
num=np.array(ls)

num=num.reshape(1,-1)

with open(xg,'rb') as file:
    x1=pickle.load(file)

num=ss.transform(num)
pred=x1.predict(num)