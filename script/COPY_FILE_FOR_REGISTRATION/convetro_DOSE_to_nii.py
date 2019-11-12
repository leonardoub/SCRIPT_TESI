#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:06:37 2019

@author: leonardo
"""

import dicom2nifti
import os
import argparse

def DICOM_to_nii_converter(folder_path, ending, output_path):
    
        for dirpath, dirnames, filenames in os.walk(folder):
            for filename in filenames:
                if filename.endswith(ending):
                    full_name = os.path.join(dirpath, filename)
    
    
    '/home/leonardo/Documenti/TESI/file_for_registration_2/Patient01'