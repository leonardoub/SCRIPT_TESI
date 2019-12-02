#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 23:32:51 2019

@author: leonardo
"""

import numpy as np
import json 
import pandas as pd

#json_path = '/home/leonardo/Scrivania/TESI/dati/MRI_DWI_nii/Patient02_AIM02/Patient02_AIM02_MR_2011-09-07_101859_Rm.cranioencefalo.con.m.d.c-_DWI.HR.E_n160__00000/-a.json'
#bvec_path = '/home/leonardo/Scrivania/TESI/dati/MRI_DWI_nii/Patient02_AIM02/Patient02_AIM02_MR_2011-09-07_101859_Rm.cranioencefalo.con.m.d.c-_DWI.HR.E_n160__00000/-a.bvec'
#bval_path = '/home/leonardo/Scrivania/TESI/dati/MRI_DWI_nii/Patient02_AIM02/Patient02_AIM02_MR_2011-09-07_101859_Rm.cranioencefalo.con.m.d.c-_DWI.HR.E_n160__00000/-a.bval'
#

json_path = '/home/leonardo/Scrivania/MRI_DWI_nii/Patient02_AIM02/Patient02_AIM02_MR_2011-09-07_101859_Rm.cranioencefalo.con.m.d.c-_DWI.HR.E_n160__00000/-a.json'
bvec_path = '/home/leonardo/Scrivania/MRI_DWI_nii/Patient02_AIM02/Patient02_AIM02_MR_2011-09-07_101859_Rm.cranioencefalo.con.m.d.c-_DWI.HR.E_n160__00000/-a.bvec'
bval_path = '/home/leonardo/Scrivania/MRI_DWI_nii/Patient02_AIM02/Patient02_AIM02_MR_2011-09-07_101859_Rm.cranioencefalo.con.m.d.c-_DWI.HR.E_n160__00000/-a.bval'


with open(json_path) as json_file:
    A = json.load(json_file)

print(bval_path)
print(bvec_path)
print(json_path)

    
with open(json_path) as json_file:
     print(json_path)
     print(json_file)

     A = json.load(json_file)




B = np.loadtxt(bvec_path)
Bt = B.T
sp = np.shape(Bt)[0]
Bt_sp = np.vsplit(Bt, sp)
dict_bvec = {f'Direzione {i} bvec': Bt_sp[i] for i in range(sp)}

 
C = np.loadtxt(bval_path) 
Ct = C.T
dict_bval = {'bval' : Ct}


#A.update({'bvec': Bt_sp})
#A.update({'bval': Ct})
#

interesting_keys = ['Manufacturer', 'ManufacturersModelName', 'ProtocolName']

new_dict = {key : A[key] for key in interesting_keys}

my_dict_02 = {**new_dict, **dict_bvec, **dict_bval}

bvec_keys = list(dict_bvec.keys())



json_path_03 = '/home/leonardo/Scrivania/TESI/dati/MRI_DWI_nii/Patient03_AIM03/Patient03_AIM03_MR_2012-01-11_174451_Rm.cranioencefalo.con.m.d.c-_DWI.HR_n120__00000/-a.json'
bvec_path_03 = '/home/leonardo/Scrivania/TESI/dati/MRI_DWI_nii/Patient03_AIM03/Patient03_AIM03_MR_2012-01-11_174451_Rm.cranioencefalo.con.m.d.c-_DWI.HR_n120__00000/-a.bvec'
bval_path_03 = '/home/leonardo/Scrivania/TESI/dati/MRI_DWI_nii/Patient03_AIM03/Patient03_AIM03_MR_2012-01-11_174451_Rm.cranioencefalo.con.m.d.c-_DWI.HR_n120__00000/-a.bval'


#json_path_03 = '/home/leonardo/Scrivania/MRI_DWI_nii/Patient03_AIM03/Patient03_AIM03_MR_2012-01-11_174451_Rm.cranioencefalo.con.m.d.c-_DWI.HR_n120__00000/-a.json'
#bvec_path_03 = '/home/leonardo/Scrivania/MRI_DWI_nii/Patient03_AIM03/Patient03_AIM03_MR_2012-01-11_174451_Rm.cranioencefalo.con.m.d.c-_DWI.HR_n120__00000/-a.bvec'
#bval_path_03 = '/home/leonardo/Scrivania/MRI_DWI_nii/Patient03_AIM03/Patient03_AIM03_MR_2012-01-11_174451_Rm.cranioencefalo.con.m.d.c-_DWI.HR_n120__00000/-a.bval'


with open(json_path_03) as json_file:
    A_03 = json.load(json_file)


B_03 = np.loadtxt(bvec_path_03)
Bt_03 = B_03.T
sp_03 = np.shape(Bt_03)[0]
Bt_03_sp = np.vsplit(Bt_03, sp_03)

dict_bvec_03 = {f'Direzione {i} bvec': Bt_03_sp[i] for i in range(sp_03)}
 
C_03 = np.loadtxt(bval_path_03) 
Ct_03 = C_03.T
dict_bval_03 = {'bval' : Ct_03}


#A.update({'bvec': Bt_sp})
#A.update({'bval': Ct})
#

interesting_keys_03 = ['Manufacturer', 'ManufacturersModelName', 'ProtocolName']

new_dict_03 = {key : A_03[key] for key in interesting_keys}

my_dict_03 = {**new_dict_03, **dict_bvec_03, **dict_bval_03}

bvec_keys = list(dict_bvec.keys())

###FARE PROVA CON QUALCUNO CON PIÙ GRADIENTI


json_path_55 = '/home/leonardo/Scrivania/TESI/dati/MRI_DWI_nii/Patient55_AIM55/Patient55_AIM55_MR_2017-09-28_081424_rm.encefalo.+.midollo.mdc_Reg.-.DWI.HR.SENSE_n540__00000/-a.json'
bvec_path_55 = '/home/leonardo/Scrivania/TESI/dati/MRI_DWI_nii/Patient55_AIM55/Patient55_AIM55_MR_2017-09-28_081424_rm.encefalo.+.midollo.mdc_Reg.-.DWI.HR.SENSE_n540__00000/-a.bvec'
bval_path_55 = '/home/leonardo/Scrivania/TESI/dati/MRI_DWI_nii/Patient55_AIM55/Patient55_AIM55_MR_2017-09-28_081424_rm.encefalo.+.midollo.mdc_Reg.-.DWI.HR.SENSE_n540__00000/-a.bval'


#json_path_55 = '/home/leonardo/Scrivania/MRI_DWI_nii/Patient55_AIM55/Patient55_AIM55_MR_2017-09-28_081424_rm.encefalo.+.midollo.mdc_Reg.-.DWI.HR.SENSE_n540__00000/-a.json'
#bvec_path_55 = '/home/leonardo/Scrivania/MRI_DWI_nii/Patient55_AIM55/Patient55_AIM55_MR_2017-09-28_081424_rm.encefalo.+.midollo.mdc_Reg.-.DWI.HR.SENSE_n540__00000/-a.bvec'
#bval_path_55 = '/home/leonardo/Scrivania/MRI_DWI_nii/Patient55_AIM55/Patient55_AIM55_MR_2017-09-28_081424_rm.encefalo.+.midollo.mdc_Reg.-.DWI.HR.SENSE_n540__00000/-a.bval'


with open(json_path_55) as json_file:
    A_55 = json.load(json_file)


B_55 = np.loadtxt(bvec_path_55)
Bt_55 = B_55.T
sp_55 = np.shape(Bt_55)[0]
Bt_55_sp = np.vsplit(Bt_55, sp_55)

dict_bvec_55 = {f'Direzione {i} bvec': Bt_55_sp[i] for i in range(sp_55)}
 
C_55 = np.loadtxt(bval_path_55) 
Ct_55 = C_55.T
dict_bval_55 = {'bval' : Ct_55}

#A.update({'bvec': Bt_sp})
#A.update({'bval': Ct})
#

interesting_keys_55 = ['Manufacturer', 'ManufacturersModelName', 'ProtocolName']

new_dict_55 = {key : A_55[key] for key in interesting_keys}

my_dict_55 = {**new_dict_55, **dict_bvec_55, **dict_bval_55}

bvec_keys = list(dict_bvec_55.keys())
bval_keys = list(dict_bval_55.keys())

D={'Patient02': my_dict_02, 'Patient03': my_dict_03, 'Patient55': my_dict_55}


K=pd.DataFrame.from_dict(D, orient='index', columns=interesting_keys+bvec_keys+bval_keys)















