# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import SimpleITK as sitk


Mask_path='/home/leonardo/Scrivania/data_registered/Patient06/MASK_TOT.nii'
Maskstk=sitk.ReadImage(Mask_path)


#mask_size=Maskstk.GetSize()
#mask_spacing=Maskstk.GetSpacing()
#mask_depth=Maskstk.GetDepth()
#mask_dimension=Maskstk.GetDimension()
#mask_direction=Maskstk.GetDirection()
#mask_numberofpixels=Maskstk.GetNumberOfPixels()
#mask_origin=Maskstk.GetOrigin()


Masknp=sitk.GetArrayFromImage(Maskstk)

num_slices = Masknp.shape[0]

for z in range(num_slices):
    A = sum(Masknp[:,:,z])
    print(A)
    
    
    
    











Imagestk_1.SetSpacing(mask_spacing)
Imagestk_1.SetDirection(mask_direction)
Imagestk_1.SetOrigin(mask_origin)



sitk.WriteImage(MaskTOT_stk, output_path, True)