# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import SimpleITK as sitk


Mask_path='/home/leonardo/Scrivania/data_registered/Patient52/MASK_TOT.nii'
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

A = Masknp.sum(axis=(1,2)) #non c'è bisogno di un ciclo for sulle slices, lo fa da solo


indices = np.where(A >= 600)


#mask = [A[i]!=0 and A[i+10]-A[i]>=A[i] for i in range(num_slices)]
#indices = np.where(A >= 600)


index = indices[0][0]

Masknp[:,:,:index] = 0

B = Masknp.sum(axis=(1,2))



for value in A:
    if value>400:
        in







Imagestk_1.SetSpacing(mask_spacing)
Imagestk_1.SetDirection(mask_direction)
Imagestk_1.SetOrigin(mask_origin)



sitk.WriteImage(MaskTOT_stk, output_path, True)