#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:29:18 2019

@author: leonardo
"""
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import SimpleITK as sitk


fig = plt.figure()
ax = fig.gca(projection='3d')

Mask_path='/home/leonardo/Scrivania/Patients/04/CSI/RT_nii/mask_Body.nii'
Maskstk=sitk.ReadImage(Mask_path)
Mask_np=sitk.GetArrayFromImage(Maskstk)

DOSE_path='/home/leonardo/Scrivania/Patients/04/DOSE TOTALE/88524_RTDOSE_2012-03-13_123432_CSI_Accumulated.Dose.BOOST.+.CSI_n1__00000/2.16.840.1.114362.1.11741058.22091046951.516567973.476.6989.dcm'  
DOSEstk=sitk.ReadImage(DOSE_path)
DOSE_scaling=DOSEstk.GetMetaData('3004|000e')

DOSE_np=sitk.GetArrayFromImage(DOSEstk)
DOSE_np1=DOSE_np*float(DOSE_scaling)

DOSE_np2=DOSE_np1*Mask_np

dim=DOSE_np.shape
X=np.arange(dim[2])
Y=np.arange(dim[1])

#X=np.arange(50,201)
#Y=np.arange(100,201)

X, Y = np.meshgrid(X, Y)

Max_DOSE=np.max(DOSE_np2)
ind=np.where(DOSE_np2==Max_DOSE)

DOSE=DOSE_np2[int(ind[0]),:,:]
#DOSE=DOSE_np2[int(ind[0]),100:201,50:201]

surf=ax.plot_surface(X,Y,DOSE, cmap=cm.jet, linewidth=0, antialiased=False)


cbar=fig.colorbar(surf, shrink=0.5, aspect=5)

cbar.set_label('Dose [Gy]',labelpad=-35)

plt.savefig('/home/leonardo/Scrivania/Patients/04/plot/surface_jet_mask_PTV_Body.pdf')



#NON POSSO USARE LE ROI PERCHÈ SUCCEDE DEL CASINO CI SONO PROBLEMI SI ALLINEAMENTO LUNGO Z ANCHE SE LE IMMAGINI HANNO LE STESSE DIMENSIONI







#plt.plot(DOSE_np)
