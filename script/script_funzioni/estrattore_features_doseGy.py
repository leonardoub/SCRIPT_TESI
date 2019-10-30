#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:57:50 2019

@author: leonardo
"""

import radiomics
import SimpleITK as sitk
from radiomics import featureextractor


def EstrattoreFeaturesDose(Image_path,Mask_path,Output_path):
    Maskstk=sitk.ReadImage(Mask_path)
    Imagestk=sitk.ReadImage(Image_path)
    
    
    DOSE_size=Imagestk.GetSize()
    DOSE_spacing=Imagestk.GetSpacing()
    DOSE_depth=Imagestk.GetDepth()
    DOSE_dimension=Imagestk.GetDimension()
    DOSE_direction=Imagestk.GetDirection()
    DOSE_numberofpixels=Imagestk.GetNumberOfPixels()
    DOSE_origin=Imagestk.GetOrigin()
    DOSE_scaling=Imagestk.GetMetaData('3004|000e')

    
    
    Imagestk_np=sitk.GetArrayFromImage(Imagestk)
    Imagestk_np1=Imagestk_np*float(DOSE_scaling)
    Imagestk_1=sitk.GetImageFromArray(Imagestk_np1)
    
        
    Imagestk_1.SetSpacing(DOSE_spacing)
    Imagestk_1.SetDirection(DOSE_direction)
    Imagestk_1.SetOrigin(DOSE_origin)
    
    extractor=featureextractor.RadiomicsFeatureExtractor(binWidth=1, correctMask=True)
    result=extractor.execute(Imagestk_1,Maskstk)
    
    import pandas as pd
    
    features={}

    for key,value in result.items():
        features[key]=value
    
    df=pd.DataFrame(result.items())
    df.to_csv(Output_path)
        
        
        
        
        
    