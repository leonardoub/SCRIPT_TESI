#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 09:13:56 2019

@author: leonardo
"""

from dcmrtstruct2nii import dcmrtstruct2nii

PathDicom_CT= '/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/Patient16/Patient16_AIM16_CT_2013-10-25_112558_CSI.CB.MM_kVCT.Image.Set_n223__00000'

RT= '/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/Patient16/Patient16_AIM16_RTst_2013-10-25_112558_CSI.CB.MM_TomoTherapy.Structure.Set_n1__00000/2.16.840.1.114362.1.11741058.22091046951.521051285.560.4603.dcm'

output_path='/home/leonardo/Scrivania/RT_nii/'

dcmrtstruct2nii(RT,PathDicom_CT,output_path,structures=None,gzip=False,mask_background_value=0,mask_foreground_value=1,convert_original_dicom=True)