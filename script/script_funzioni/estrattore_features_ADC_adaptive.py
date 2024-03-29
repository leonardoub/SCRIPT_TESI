#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 19:36:48 2019

@author: leonardo
"""

import radiomics
from radiomics import featureextractor
import SimpleITK as sitk
import argparse
import pandas as pd
import numpy as np


def EstrattoreFeaturesADC(path_list, number_of_bin):
    
    list_path = [line.split() for line in open(path_list, 'r')]
    
    
    for i in range(len(list_path)):
        
        Output_path = list_path[i][2]
        Mask_path = list_path[i][1]
        Image_path = list_path[i][0]
        
        print(Output_path)
        print(Mask_path)
        print(Image_path)

    
        Maskstk = sitk.ReadImage(Mask_path)
        Imagestk = sitk.ReadImage(Image_path)  

        
        Imagestk_np = sitk.GetArrayFromImage(Imagestk)
        Maskstk_np = sitk.GetArrayFromImage(Maskstk) 
        Imagestk_np_with_mask = Imagestk_np*Maskstk_np
        Max = np.max(Imagestk_np_with_mask)
        Min = np.min(Imagestk_np_with_mask)
        
        bin_Width = (Max-Min)/number_of_bin
                
        extractor = featureextractor.RadiomicsFeatureExtractor(binWidth=bin_Width, correctMask=True)
        result = extractor.execute(Imagestk, Maskstk)
    
    
        features = {}

        for key, value in result.items():
            features[key] = value
    
        df = pd.DataFrame(result.items())
        df.to_csv(Output_path)
        
if __name__=="__main__":
    descr = 'Extraction features from image with a given mask. Image path, mask path and output path must be in a list with 3 columns' 
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument('path_list_path', type=str,
                    help='the path of list of path')
    parser.add_argument('bin_number', type=int, 
                    help='bin number of the istogram. Number of bins must be between 30 and 130')
    parser.add_argument('-v', '--verbosity', type=int,
                        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default=0, help='increase verbosity of the output')
    args = parser.parse_args()           

    radiomics.setVerbosity(args.verbosity)

    EstrattoreFeaturesADC(args.path_list_path, args.bin_number)
       
    
    
    