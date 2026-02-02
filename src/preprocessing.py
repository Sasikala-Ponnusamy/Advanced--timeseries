import numpy as np
from sklearn.preprocessing import MinMaxScaler
def preprocess(df,target_col].fillna(method='ffill')
    scaler=MinMaxScaler()
    scaled=scaler.fit_transform(df[[target_col]])
    X,y=[],[]
    for i in range(window,len(scaled)):
      X.append(scaled[i-window:i])
      y.append(scaled[i])
    return np.array,np.array(y),scaler  
