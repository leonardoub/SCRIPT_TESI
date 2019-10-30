#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 09:13:56 2019

@author: leonardo
"""

from dcmrtstruct2nii import dcmrtstruct2nii

RT='/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/Patient35/2015/Patient35_AIM35_RTst_2015-08-10_112038_CSI_TomoTherapy.Structure.Set_n1__00000/2.16.840.1.114362.1.11741058.22091046951.521052423.1038.1492.dcm' 
PathDicom_CT= '/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/Patient35/2015/Patient35_AIM35_CT_2015-08-10_112038_CSI_kVCT.Image.Set_n227__00000'

output_path='/home/leonardo/Scrivania/TESI/dati/pazienti_20190725/Patients_Anonymized+RTstnii/Patient35/RT_nii/'

dcmrtstruct2nii(RT,PathDicom_CT,output_path,structures=None,gzip=False,mask_background_value=0,mask_foreground_value=1,convert_original_dicom=True)