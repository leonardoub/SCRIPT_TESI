#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 18:31:23 2019

@author: leonardo
"""

import numpy as np
import SimpleITK as sitk


CSI_path='/home/leonardo/Scrivania/Patients/93848/CSI/93848_RTDOSE_2014-07-22_105925_CSI.EML.CG_TomoTherapy.Planned.Dose_n1__00000/1.2.826.0.1.3680043.2.200.29706027.343.59398.2637.dcm'
Boost_path='/home/leonardo/Scrivania/Patients/93848/BOOST FCP/93848_RTDOSE_2014-07-22_105925_CSI.EML.CG_TomoTherapy.Planned.Dose_n1__00000/1.2.826.0.1.3680043.2.200.15466527.789.70379.2319.dcm'
DoseTOT_path='/home/leonardo/Scrivania/Patients/93848/DOSE TOTALE/93848_RTDOSE_2014-07-22_105925_CSI.EML.CG_Accumulated.Dose.BOOSTs.+.CSI_n1__00000/2.16.840.1.114362.1.11741058.22091046951.517538301.990.5971.dcm'

CSIstk=sitk.ReadImage(CSI_path)
Booststk=sitk.ReadImage(Boost_path)
DoseTOTstk=sitk.ReadImage(DoseTOT_path)

CSInp=sitk.GetArrayFromImage(CSIstk)
Boostnp=sitk.GetArrayFromImage(Booststk)
DoseTOTnp=sitk.GetArrayFromImage(DoseTOTstk)

