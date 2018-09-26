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
    
    # delete Nan Values & reset index
    new_df = new_df.dropna(axis=0)
    new_df = new_df.reset_index()
    
    # data divide
    input_data = new_df['input']
    output_data = new_df['output']
    
    print('input_data size: ', len(input_data))
    print('output_data size: ', len(output_data))
    # write .txt file until input data size 
    f = open("data/user-nuguri.txt",'w')
    for i in range(len(input_data)):
        indata = input_data[i] + '\t' + output_data[i] + '\n'
        f.write(indata)

    print('finished. please check data/user-nuguri.txt. ')
