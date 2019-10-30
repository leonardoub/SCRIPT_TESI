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


def update_plot1( frn, DOSE_np1, plot1):
    plot1[0].remove()
    plot1[0] = ax.plot_surface(X, Y, DOSE_np1[frn,:,:], cmap="jet")

def update_plot2( frn, CT_np, plot2):
    plot2[0].remove()
    plot2[0] = ax.plot_surface(X, Y, CT_np[frn,:,:])


fps = 10 # frame per sec

fig = plt.figure()


fig, (ax1, ax2) = plt.subplots(1, 2)

ax1 = fig.gca(projection='3d')


#fig.set_size_inches(15, 7)

CT_path='/home/leonardo/Scrivania/Patients/03/CSI/88203_CT_2012-01-31_103006_CRANIO.SPINALE.....AM_kVCT.Image.Set_n324__00000'
CTstk=sitk.ReadImage(CT_path)
CT_np=sitk.GetArrayFromImage(CTstk)


DOSE_path='/home/leonardo/Scrivania/Patients/03/DOSE TOTALE/88203_RTDOSE_2012-01-31_103006_CRANIO.SPINALE.....AM_Accumulated.Dose.BOOSTs.+.CSI_n1__00000/2.16.840.1.114362.1.11741058.22091046951.516569053.366.9703.dcm'  
DOSEstk=sitk.ReadImage(DOSE_path)
DOSE_scaling=DOSEstk.GetMetaData('3004|000e')

DOSE_np=sitk.GetArrayFromImage(DOSEstk)
DOSE_np1=DOSE_np*float(DOSE_scaling)


dim=DOSE_np.shape
X=np.arange(dim[2])
Y=np.arange(dim[1])

X, Y = np.meshgrid(X, Y)


DOSE=DOSE_np1[0,:,:]


plot1=[ax1.plot_surface(X,Y,DOSE, cmap=cm.coolwarm, linewidth=0, antialiased=False)]

ax1.set_zlim(np.min(DOSE_np1),np.max(DOSE_np1))

plot2=[ax2.pl]

#
#cbar=fig.colorbar(fig, shrink=0.5, aspect=5)
#
#cbar.set_label('Dose [Gy]',labelpad=-35)


frn=dim[0] # frame number of the animation


ani1 = animation.FuncAnimation(fig, update_plot1, frn, fargs=(DOSE_np1, plot1), interval=1000/fps)

ani2 = animation.FuncAnimation(fig, update_plot2, frn, fargs=(CT_np, plot2), interval=1000/fps)

ani.save('/home/leonardo/Scrivania/Patients/03/plot/animation_surface_no_mask_CT.gif', writer='imagemagick')



