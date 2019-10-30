#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 16:44:49 2019

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

def update_plot2( frn, CT_np, plot):
    plot[0].remove()
    plot[0] = fig.imshow(CT_np[frn,:,:])
    
fps = 10 # frame per sec

fig = plt.figure()


CT_path='/home/leonardo/Scrivania/Patients/03/CSI/88203_CT_2012-01-31_103006_CRANIO.SPINALE.....AM_kVCT.Image.Set_n324__00000'
CTstk=sitk.ReadImage(CT_path)
CT_np=sitk.GetArrayFromImage(CTstk)


dim=CT_np.shape
X=np.arange(dim[2])
Y=np.arange(dim[1])

X, Y = np.meshgrid(X, Y)

CT=CT_np[0,:,:]

plot=[fig.imshow(CT)]


frn=dim[0] # frame number of the animation


ani = animation.FuncAnimation(fig, update_plot2, frn, fargs=(CT_np, plot), interval=1000/fps)

ani.save('/home/leonardo/Scrivania/Patients/03/plot/animation_CT.gif', writer='imagemagick')














   