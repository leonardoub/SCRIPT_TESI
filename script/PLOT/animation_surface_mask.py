#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 12:39:40 2019

@author: leonardo
"""

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


def update_plot( frn, DOSE_np1, plot,):
    plot[0].remove()
    plot[0] = ax.plot_surface(X, Y, DOSE_np1[frn,:,:], cmap="jet")

fps = 10 # frame per sec

fig = plt.figure()
ax = fig.gca(projection='3d')



Mask_path='/home/leonardo/Scrivania/Patients/04/CSI/RT_nii/mask_PTV 39.nii'
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

X, Y = np.meshgrid(X, Y)

DOSE=DOSE_np2[0,:,:]

plot=[ax.plot_surface(X,Y,DOSE, cmap=cm.coolwarm, linewidth=0, antialiased=False)]

ax.set_zlim(np.min(DOSE_np2),np.max(DOSE_np2))


frn=dim[0] # frame number of the animation


ani = animation.FuncAnimation(fig, update_plot, frn, fargs=(DOSE_np2, plot), interval=1000/fps)

ani.save('/home/leonardo/Scrivania/Patients/04/plot/animation_surface_mask_PTV_39.gif', writer='imagemagick')



