# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import json 
import pandas as pd

path='/home/leonardo/Scrivania/MRI_DWI_nii/Patient02_AIM02/Patient02_AIM02_MR_2011-09-07_101859_Rm.cranioencefalo.con.m.d.c-_DWI.HR.E_n160__00000/-a.json'

bvec='/home/leonardo/Scrivania/MRI_DWI_nii/Patient02_AIM02/Patient02_AIM02_MR_2011-09-07_101859_Rm.cranioencefalo.con.m.d.c-_DWI.HR.E_n160__00000/-a.bvec'

with open(path) as file_:
    a=json.load(file_)

b=np.loadtxt(bvec)


a.update({'bvector': b})


TAB=pd.DataFrame.from_dict(a)
