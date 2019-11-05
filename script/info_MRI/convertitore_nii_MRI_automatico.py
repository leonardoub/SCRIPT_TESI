#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:54:03 2019

@author: leonardo
"""

import dicom2nifti
import os
import glob

dwi_path =  '/home/leonardo/Scrivania/TESI/dati/MRI_DWI/Patient55_AIM55/2017-09__Studies/Patient55_AIM55_MR_2017-09-28_081424_rm.encefalo.+.midollo.mdc_DWI.HR_n540__00000' 


dicom2nifti.dicom_series_to_nifti(dwi_path, '/home/leonardo/Scrivania/a')