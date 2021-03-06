import numpy 
import pandas
import csv
from pandas import DataFrame
from keras.models import load_model


path_test  = 'D:/data1/NN_data/export_data_x_start_test_30.csv'
output_test = pandas.read_csv(path_test)
X_test  = output_test.iloc[100000:120000,0:30]
Y_test  = output_test.iloc[100000:120000,30]

loaded_model=load_model('D:/MITECH/2020/CNN/CNN_linear/input30_60_30_1_eps6_batsz2.h5')
predictions = loaded_model.predict(X_test)

rounded = [round(x[0]) for x in predictions]
for x in range(19999):
    print(rounded[x],'====',Y_test[x+100000])




