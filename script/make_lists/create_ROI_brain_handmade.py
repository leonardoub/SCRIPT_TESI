# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#
#lista_index=[]
#lista_name=[]
import numpy as np
import SimpleITK as sitk
import argparse




N='23'
Mask_path='/home/leonardo/Scrivania/data_registered/Patient'+N+'/MASK_TOT.nii'

Output_path='/home/leonardo/Scrivania/data_registered/Patient'+N+'/MASK_BRAIN_HANDMADE.nii'

Maskstk = sitk.ReadImage(Mask_path)
        
mask_size = Maskstk.GetSize()
mask_spacing = Maskstk.GetSpacing()
mask_depth = Maskstk.GetDepth()
mask_dimension = Maskstk.GetDimension()
mask_direction = Maskstk.GetDirection()
mask_numberofpixels = Maskstk.GetNumberOfPixels()
mask_origin = Maskstk.GetOrigin()
        
Masknp = sitk.GetArrayFromImage(Maskstk)
              
A = Masknp.sum(axis=(1,2))    
 
#################################
#################################
#################################

index=246
        
Masknp[:index,:,:] = 0    
                       
Maskstk_1 = sitk.GetImageFromArray(Masknp)
        
Maskstk_1.SetSpacing(mask_spacing)
Maskstk_1.SetDirection(mask_direction)
Maskstk_1.SetOrigin(mask_origin)
        
sitk.WriteImage(Maskstk_1, Output_path, True)


lista_index.append(index)
lista_name.append(N)

#################################
#################################
#################################

import pandas as pd

df=pd.Series(data=p, index=q)
df.to_csv(r'/home/leonardo/Scrivania/indici.csv', header=True)



