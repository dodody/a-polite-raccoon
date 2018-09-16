import pandas as pd
import numpy as np

import sys

if len(sys.argv)==2 :
    csv_file_name = sys.argv[1]

    ### 1. read csv
    # Please Download Google Spread Sheet 
    # intput Google Spread Sheet Name 
    data = pd.read_csv(csv_file_name)
    
    # data divide
    input_data = data.iloc[:,0]
    output_data = data.iloc[:,1]
    
    # make new Dataframe
    new_df = pd.DataFrame({'input': input_data, 'output': output_data})
    
    # delete Nan Values
    new_df.dropna()

    # data divide
    input_data = new_df.iloc[:0]
    output_data = new_df.iloc[:1]

    # write .txt file until input data size 
    f = open("data/user-nuguri.txt",'w')
    for i in range(len(input_data)):
        indata = input_data[i] + '\t' + output_data[i] + '\n'
        f.write(indata)
