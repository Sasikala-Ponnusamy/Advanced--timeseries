from tensorflow.keras.models import Sequential
from tensorflow.layers import LSTM,Dense
def build_model(input_shape,units):
  model=Sequential([LSTM(units,activation='relu',input_shape=input_shape),Dense(1)])
  model.compile(optimizer='adam',loss='mse')
  return model
