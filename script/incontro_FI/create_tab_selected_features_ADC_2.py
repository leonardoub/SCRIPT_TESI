#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:32:24 2019

@author: leonardo
"""

import os
import glob
import pandas as pd
import argparse


def create_tab_selected_features(folder_path, output_path, interesting_features)

A = glob.glob(folder_path+os.sep+'*')
A.sort()

interesting_features = ['original_firstorder_Minimum', 'original_firstorder_Maximum', 
                        'original_firstorder_MeanAbsoluteDeviation', 'original_firstorder_Mean', 
                        'original_firstorder_Median', 'original_firstorder_Range','original_firstorder_Variance']

D = {}

for i in A:
    
    patient = i.split(os.sep)[-1].replace('.csv', '')
    
    df = pd.read_csv(i)
    
    feature_names=list(df.iloc[:,1])
    feature_value=list(df.iloc[:,2])
    
    df_pat=pd.Series(data=feature_value, index=feature_names)
    
    dict_features=df_pat.to_dict()
    
    dict_selected_features = {key : dict_features[key] for key in interesting_features}

    D.update({patient : dict_selected_features})
    
K=pd.DataFrame.from_dict(D, orient='index', columns=interesting_features)


K.to_csv(output_path, header=True)







#original_firstorder_Minimum
#
#original_firstorder_Maximum
#
#original_firstorder_MeanAbsoluteDeviation
#
#original_firstorder_Mean
#
#original_firstorder_Median
#
#original_firstorder_Range
#
#original_firstorder_Variance