#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 09:35:45 2019

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

#fig.set_size_inches(15, 7)

DOSE_path='/home/leonardo/Scrivania/Patients/06/DOSE TOTALE/89030_RTDOSE_2012-06-19_102031_CSI.MDC....RG_Accumulated.Dose.BOOST.+.CSI_n1__00000/2.16.840.1.114362.1.11741058.22091046951.516568254.780.8131.dcm'  
DOSEstk=sitk.ReadImage(DOSE_path)
DOSE_scaling=DOSEstk.GetMetaData('3004|000e')

DOSE_np=sitk.GetArrayFromImage(DOSEstk)
DOSE_np1=DOSE_np*float(DOSE_scaling)


dim=DOSE_np.shape
X=np.arange(dim[2])
Y=np.arange(dim[1])

X, Y = np.meshgrid(X, Y)


DOSE=DOSE_np1[0,:,:]


plot=[ax.plot_surface(X,Y,DOSE, cmap=cm.coolwarm, linewidth=0, antialiased=False)]

ax.set_zlim(np.min(DOSE_np1),np.max(DOSE_np1))

#
#cbar=fig.colorbar(fig, shrink=0.5, aspect=5)
#
#cbar.set_label('Dose [Gy]',labelpad=-35)


frn=dim[0] # frame number of the animation


ani = animation.FuncAnimation(fig, update_plot, frn, fargs=(DOSE_np1, plot), interval=1000/fps)

ani.save('/home/leonardo/Scrivania/Patients/06/plot/animation_surface_no_mask.gif', writer='imagemagick')



