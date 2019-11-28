# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import SimpleITK as sitk
import argparse

def Mask_Cutter(path_list, stp):

    list_path = [line.split() for line in open(path_list, 'r')]
    
    
    for i in range(len(list_path)):
        
        Output_path = list_path[i][1]
        Mask_path = list_path[i][0]
        
        print(Output_path)
        print(Mask_path)
        
        #CUT MASK
        Maskstk = sitk.ReadImage(Mask_path)
        
        mask_size = Maskstk.GetSize()
        mask_spacing = Maskstk.GetSpacing()
        mask_depth = Maskstk.GetDepth()
        mask_dimension = Maskstk.GetDimension()
        mask_direction = Maskstk.GetDirection()
        mask_numberofpixels = Maskstk.GetNumberOfPixels()
        mask_origin = Maskstk.GetOrigin()
        
        Masknp = sitk.GetArrayFromImage(Maskstk)
        
        num_slices = Masknp.shape[0]
        
        A = Masknp.sum(axis=(1,2)) #non c'è bisogno di un ciclo for sulle slices, lo fa da solo
        
        ##selezione a soglia
        #indices = np.where(A >= 600)
        #index = indices[0][0]
        
#        mask = [A[i]>A[i-1]>A[i-2]>A[i-3]>A[i-4]>A[i-5]>A[i-6]>A[i-7]>A[i-8]>A[i-9]>A[i-10] for i in range(num_slices)]
        
        mask = [np.all(A[i-stp:i]==sorted(A[i-stp:i])) and A[i]!=0 for i in range(num_slices)]

    
        B = A[mask]
        
        indices = np.where(A >= B[0])
        index = indices[0][0]
        
        Masknp[:index,:,:] = 0
        
        ##serve per controllo
        #C = Masknp.sum(axis=(1,2))
        
        Maskstk_1 = sitk.GetImageFromArray(Masknp)
        
        Maskstk_1.SetSpacing(mask_spacing)
        Maskstk_1.SetDirection(mask_direction)
        Maskstk_1.SetOrigin(mask_origin)
        
        sitk.WriteImage(Maskstk_1, Output_path, True)
        
if __name__=="__main__":
    descr = 'This program cut the CSI mask in order to obatain a Brain mask'
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument('path_of_path_list', type=str, help='Path of the list which contain 2 columns: first is about the path of CSI mask, the second is about the path where do you want to save the brain mask')
    parser.add_argument('--step', type=int, help='Length of the step', default=10)
    args = parser.parse_args()

    Mask_Cutter(args.path_of_path_list, args.step)    




#mask = [A[i+8]>A[i+7]>A[i+6]>A[i+5]>A[i+4]>A[i+3]>A[i+2]>A[i+1]>A[i] for i in range(num_slices)]


