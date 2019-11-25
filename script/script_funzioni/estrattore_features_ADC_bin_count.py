#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 19:36:48 2019

@author: leonardo
"""

from radiomics import featureextractor
import SimpleITK as sitk
import argparse
import pandas as pd


def EstrattoreFeaturesADC(path_list, bin_Count):
    
    list_path = [line.split() for line in open(path_list, 'r')]
    
    
    for i in range(len(list_path)):
        
        Output_path = list_path[i][2]
        Mask_path = list_path[i][1]
        Image_path = list_path[i][0]
    
        Maskstk = sitk.ReadImage(Mask_path)
        Imagestk = sitk.ReadImage(Image_path)    
            
        extractor = featureextractor.RadiomicsFeatureExtractor(binCount=bin_Count, correctMask=True)
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
    parser.add_argument('bin_count', type=int, 
                    help='number if the bin of the istogram. Must be between 30 and 130')
    args = parser.parse_args()           

    EstrattoreFeaturesADC(args.path_list_path, args.bin_count)
       
    
    
    