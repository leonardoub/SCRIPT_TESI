#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 09:13:56 2019

@author: leonardo
"""

from dcmrtstruct2nii import dcmrtstruct2nii

RT='/home/leonardo/Scrivania/paziente_prova/CSI+Boost/RTst_2011-09-29_075800_TomoTherapy.Patient.Disease_TomoTherapy.Structure.Set_n1__00000/1.2.826.0.1.3680043.2.200.868401404.495.96056.551.dcm'
PathDicom_DOSE='/home/leonardo/Scrivania/paziente_prova/CSI+Boost/RTDOSE_2011-09-29_075800_TomoTherapy.Patient.Disease_TomoTherapy.Planned.Dose_n1__00000'
output_path='/home/leonardo/Scrivania/paziente_prova/RT_2_nii_(DOSE)/'

dcmrtstruct2nii(RT,PathDicom_DOSE,output_path,structures=None,gzip=False,mask_background_value=0,mask_foreground_value=1,convert_original_dicom=True)