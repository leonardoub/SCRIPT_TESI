#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:57:50 2019

@author: leonardo
"""

import radiomics
import SimpleITK as sitk
from radiomics import featureextractor

radiomics.setVerbosity(10)

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

    print('DOSE_size1=',DOSE_size)
    print('DOSE_spacing1=',DOSE_spacing)
    print('DOSE_dimension1=',DOSE_dimension)
    print('DOSE_direction1=',DOSE_direction)
    print('DOSE_origin1=',DOSE_origin)

    MASK_size=Maskstk.GetSize()
    MASK_spacing=Maskstk.GetSpacing()
    MASK_depth=Maskstk.GetDepth()
    MASK_dimension=Maskstk.GetDimension()
    MASK_direction=Maskstk.GetDirection()
    MASK_numberofpixels=Maskstk.GetNumberOfPixels()
    MASK_origin=Maskstk.GetOrigin()


    print('MASK_size1=',MASK_size)
    print('MASK_spacing1=',MASK_spacing)
    print('MASK_dimension1=',MASK_dimension)
    print('MASK_direction1=',MASK_direction)
    print('MASK_origin1=',MASK_origin)


    
    Imagestk_np=sitk.GetArrayFromImage(Imagestk)
    Imagestk_np1=Imagestk_np*float(DOSE_scaling)
    Imagestk_1=sitk.GetImageFromArray(Imagestk_np1)
    
        
    Imagestk_1.SetSpacing(DOSE_spacing)
    Imagestk_1.SetDirection(DOSE_direction)
    Imagestk_1.SetOrigin(DOSE_origin)
    
     
    DOSE_size2=Imagestk_1.GetSize()
    DOSE_spacing2=Imagestk_1.GetSpacing()
    DOSE_depth2=Imagestk_1.GetDepth()
    DOSE_dimension2=Imagestk_1.GetDimension()
    DOSE_direction2=Imagestk_1.GetDirection()
    DOSE_numberofpixels2=Imagestk_1.GetNumberOfPixels()
    DOSE_origin2=Imagestk_1.GetOrigin()
    


    print('DOSE_size2=',DOSE_size2)
    print('DOSE_spacing2=',DOSE_spacing2)
    print('DOSE_dimension2=',DOSE_dimension2)
    print('DOSE_direction2=',DOSE_direction2)
    print('DOSE_origin2=',DOSE_origin2)

    
    extractor=featureextractor.RadiomicsFeatureExtractor(binCount=144352, correctMask=True)
    result=extractor.execute(Imagestk_1,Maskstk)
    
    import pandas as pd
    
    features={}

    for key,value in result.items():
        features[key]=value
    
    df=pd.DataFrame(result.items())
    df.to_csv(Output_path)
        
        
        
        
        
    