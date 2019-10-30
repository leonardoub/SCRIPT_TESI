#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 17:24:44 2019

@author: leonardo
"""

import SimpleITK as sitk
from radiomics import featureextractor


def EstrattoreFeaturesCT(Image_path, Mask_path, Output_path, bW):
    Maskstk=sitk.ReadImage(Mask_path)
    Imagestk=sitk.ReadImage(Image_path)
        
    extractor=featureextractor.RadiomicsFeatureExtractor(binWidth=bW, correctMask=True)
    result=extractor.execute(Imagestk, Maskstk)
    
    import pandas as pd
    
    features={}

    for key,value in result.items():
        features[key]=value
    
    df=pd.DataFrame(result.items())
    df.to_csv(Output_path)
        
        
   