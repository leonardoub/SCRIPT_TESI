#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:01:34 2019

@author: leonardo
"""

import matplotlib.pyplot as plt
import numpy as np
import SimpleITK as sitk


DOSE_path='/home/leonardo/Scrivania/Patients/04/DOSE TOTALE/88524_RTDOSE_2012-03-13_123432_CSI_Accumulated.Dose.BOOST.+.CSI_n1__00000/2.16.840.1.114362.1.11741058.22091046951.516567973.476.6989.dcm'  
DOSEstk=sitk.ReadImage(DOSE_path)
DOSE_scaling=DOSEstk.GetMetaData('3004|000e')

DOSE_np=sitk.GetArrayFromImage(DOSEstk)
DOSE_np1=DOSE_np*float(DOSE_scaling)

Max_DOSE=np.max(DOSE_np1)
ind=np.where(DOSE_np1==Max_DOSE)

DOSE=DOSE_np1[int(ind[0]),:,:]

plt.imshow(DOSE, cmap='jet')
plt.colorbar()

plt.savefig('/home/leonardo/Scrivania/Patients/04/plot/heatmap/plot_heatmap_no_mask.pdf',  bbox_inches = "tight")
plt.close()  




