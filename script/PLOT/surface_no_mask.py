#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 16:49:28 2019

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


DOSE_path='/home/leonardo/Scrivania/Patients/04/DOSE TOTALE/88524_RTDOSE_2012-03-13_123432_CSI_Accumulated.Dose.BOOST.+.CSI_n1__00000/2.16.840.1.114362.1.11741058.22091046951.516567973.476.6989.dcm'  
DOSEstk=sitk.ReadImage(DOSE_path)
DOSE_scaling=DOSEstk.GetMetaData('3004|000e')

DOSE_np=sitk.GetArrayFromImage(DOSEstk)
DOSE_np1=DOSE_np*float(DOSE_scaling)


dim=DOSE_np.shape
X=np.arange(dim[2])
Y=np.arange(dim[1])

X, Y = np.meshgrid(X, Y)

Max_DOSE=np.max(DOSE_np1)
ind=np.where(DOSE_np1==Max_DOSE)

DOSE=DOSE_np1[int(ind[0]),:,:]

surf=ax.plot_surface(X,Y,DOSE, cmap=cm.jet, linewidth=0, antialiased=False)

#ax.set_zlabel('Dose [Gy]')

#ax.xaxis.set_tick_params(rotation=45)
#
#ax.yaxis.set_tick_params(rotation=45)


cbar=fig.colorbar(surf, shrink=0.5, aspect=5)

cbar.set_label('Dose [Gy]',labelpad=-35)

plt.savefig('/home/leonardo/Scrivania/Patients/04/plot/surface_jet_no_mask.pdf')

