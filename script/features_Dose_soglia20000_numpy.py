#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 19:29:03 2019

@author: leonardo
"""
#voglio provare ad estrarre features dalla dose senza considerare la maschera ma considerando una soglia di 20000

import numpy as np
import SimpleITK as sitk

DOSE_path='/home/leonardo/Scrivania/paziente_prova/CSI+Boost/RTDOSE_2011-09-29_075800_TomoTherapy.Patient.Disease_TomoTherapy.Planned.Dose_n1__00000/1.2.826.0.1.3680043.2.200.426397767.89.47755.958.dcm' 
DOSEstk=sitk.ReadImage(DOSE_path)


DOSEnp=sitk.GetArrayFromImage(DOSEstk)

DOSEnp1=np.sort(DOSEnp, axis=None)
DOSEnp2=DOSEnp1[DOSEnp1.nonzero()]


Min=DOSEnp2[0]

Media=np.mean(DOSEnp2)

Max=np.max(DOSEnp2)

stdv=np.std(DOSEnp2)

#senza soglia i valori non tornano

#mettiamo una soglia a 20000 --> secondo me non tornano comunque perchè ad esempio già il minimo viene perso, però magari il numero di voxel interessanti viene simile al numero dei voxel della mask che hanno valore 1

#prendiamo i valori di DOSEno2 che sono maggiori di 20000

DOSEnp3=DOSEnp2[np.where(DOSEnp2>=20000)]


Min1=DOSEnp3[0]

Media1=np.mean(DOSEnp3)

Max1=np.max(DOSEnp3)

stdv1=np.std(DOSEnp3)

#non va bene
