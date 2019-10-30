#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 13:31:38 2019

@author: leonardo
"""


#
#import os
#os.chdir('/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii')
#patient_list=os.listdir()
#
#for patient in patient_list:
#    
#    os.remove('/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/' + patient + '/RT_nii/TOT_MOD.nii')
#    
#    
    
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt


CT_path = '/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/Patient01/RT_nii/image.nii'
CTstk=sitk.ReadImage(CT_path)
CTnp=sitk.GetArrayFromImage(CTstk)


Mask_path = '/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/Patient01/RT_nii/TOT.nii'
Maskstk=sitk.ReadImage(Mask_path)
Masknp=sitk.GetArrayFromImage(Maskstk)

Mask_path_MOD = '/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/Patient01/RT_nii/MOD.nii'
Maskstk_MOD = sitk.ReadImage(Mask_path_MOD)
Masknp_MOD=sitk.GetArrayFromImage(Maskstk_MOD)


Mask_path_MOD2 = '/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/Patient01/RT_nii/MOD2.nii'
Maskstk_MOD2 = sitk.ReadImage(Mask_path_MOD2)
Masknp_MOD2=sitk.GetArrayFromImage(Maskstk_MOD2)

    
A=CTnp*Masknp
a=A.reshape(-1)
a=a[a!=0]
a.sort()
    
B=CTnp*Masknp_MOD
b=B.reshape(-1)
b=b[b!=0]
b.sort()
    
C=CTnp*Masknp_MOD2
c=C.reshape(-1)
c=c[c!=0]
c.sort()
    


plt.hist(a, bins=100)
#plt.xticks(np.arange(-1000, 1001, step=250))
#plt.yticks(np.arange(0, 100001, step=20000))
plt.xlim(-1000, 1000)
plt.ylim(0, 100000)
plt.xlabel('H.U.')
plt.title('senza soglia')
plt.show()



plt.hist(b, bins=100)
#plt.xticks(np.arange(-1000, 1001, step=250))
#plt.yticks(np.arange(0, 100001, step=20000))
plt.xlim(-1000, 1000)
plt.ylim(0, 100000)
plt.xlabel('H.U.')
plt.title('valori inferiori 65 H.U.')
plt.show()



plt.hist(c, bins=100)
#plt.xticks(np.arange(-1000, 1001, step=250))
#plt.yticks(np.arange(0, 100001, step=20000))
plt.xlim(-1000, 1000)
plt.ylim(0, 100000)
plt.xlabel('H.U.')
plt.title('valori tra -100 e 65 H.U.')
plt.show()



