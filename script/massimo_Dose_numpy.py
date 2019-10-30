#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 09:32:45 2019

@author: leonardo
"""

#controllo valore massimo dose usando Numpy

import numpy as np
import SimpleITK as sitk

Image_path='/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/Patient10/Patient10_AIM10_RTDOSE_2013-04-08_113427_CSI_Accumulated.Dose.BOOST.+.CSI_n1__00000/2.16.840.1.114362.1.11741058.22091046951.521051032.1081.3174.dcm' 
Imagestk=sitk.ReadImage(Image_path)

Image_np=sitk.GetArrayFromImage(Imagestk)
Max=np.max(Image_np)

A=Max*9.63455298915*(10**-4)