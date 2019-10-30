#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 18:07:30 2019

@author: leonardo
"""

#programma per convertire le strutture dal formato DICOM al fomaro nii

from dcmrtstruct2nii import dcmrtstruct2nii

def convertitoreRTstDCtoNII(PathDicom_RT,PathDicom_CT,output_path):
    return dcmrtstruct2nii(PathDicom_RT, PathDicom_CT, output_path,structures=None,gzip=False,mask_background_value=0, mask_foreground_value=1,convert_original_dicom=True)
    


#convertitoreRTstDCtoNII('/home/leonardo/Scrivania/paziente_prova/CSI+Boost/RTst_2011-09-29_075800_TomoTherapy.Patient.Disease_TomoTherapy.Structure.Set_n1__00000/1.2.826.0.1.3680043.2.200.868401404.495.96056.551.dcm','/home/leonardo/Scrivania/paziente_prova/CSI+Boost/CT_2011-09-29_075800_TomoTherapy.Patient.Disease_kVCT.Image.Set_n232__00000','/home/leonardo/Scrivania/paziente_prova/RT_3_nii/')

#path='/home/leonardo/Scrivania/Patients/92073/CSI/'

#convertitoreRTstDCtoNII(path+'87517/CSI+Boost/87517_RTst_2011-09-29_075800_TomoTherapy.Patient.Disease_TomoTherapy.Structure.Set_n1__00000/1.2.826.0.1.3680043.2.200.868401404.495.96056.551.dcm', path+'87517/CSI+Boost/87517_CT',path+'87517/RT_nii/')


#convertitoreRTstDCtoNII(path+'87547/CSI+Boost/87547_RTst_2011-09-30_103324_TomoTherapy.Patient.Disease_TomoTherapy.Structure.Set_n1__00000/1.2.826.0.1.3680043.2.200.636252107.807.50664.2955.dcm', path+'87547/CSI+Boost/87547_CT_2011-09-30_103324_TomoTherapy.Patient.Disease_kVCT.Image.Set_n203__00000',path+'87547/RT_nii/')
#
#
#path='/home/leonardo/Scrivania/Patients/95654/BOOST FCP 45/'
#
#convertitoreRTstDCtoNII(path+'95654_RTst_2015-03-25_094354_CSI.LCO.CG_TomoTherapy.Structure.Set_n1__00000/1.2.826.0.1.3680043.2.200.493721479.147.81998.1064.dcm', path+'95654_CT_2015-03-25_094354_CSI.LCO.CG_kVCT.Image.Set_n337__00000',path+'RT_nii_FCP_45/')
#
#
#
#path='/home/leonardo/Scrivania/Patients/95656/BOOST FCP/'
#
#convertitoreRTstDCtoNII(path+'95656_RTst_2015-03-23_105548_CSI.LCO.PM_TomoTherapy.Structure.Set_n1__00000/1.2.826.0.1.3680043.2.200.1970218907.72.10099.1806.dcm', path+'95656_CT_2015-03-23_105548_CSI.LCO.PM_kVCT.Image.Set_n296__00000',path+'RT_nii_FCP/')
#

path='/home/leonardo/Scrivania/Patients/95656/BOOST CEREBRALE/'

convertitoreRTstDCtoNII(path+'95656_RTst_2015-03-23_105548_CSI.LCO.PM_TomoTherapy.Structure.Set_n1__00000/1.2.826.0.1.3680043.2.200.2116006860.671.10976.975.dcm', path+'95656_CT_2015-03-23_105548_CSI.LCO.PM_kVCT.Image.Set_n296__00000',path+'RT_nii_CEREBRALE/')



path='/home/leonardo/Scrivania/Patients/97247/BOOST FCP/'

convertitoreRTstDCtoNII(path+'97247_RTst_2015-10-07_093324_CSI_TomoTherapy.Structure.Set_n1__00000/1.2.826.0.1.3680043.2.200.69094006.689.61163.2743.dcm', path+'97247_CT_2015-10-07_093324_CSI_kVCT.Image.Set_n282__00000',path+'RT_nii_FCP/')
