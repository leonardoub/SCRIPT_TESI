#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 09:40:35 2019

@author: leonardo
"""

import os
import argparse

def make_parser():
    """Load a Dicom/nii/nii.gz file as Pillow image
    Arguments:
        path {str} -- filename of the dicom file to load
    Returns:
        Image -- a pillow Image
    """

    adc_end = "ADC_1.nii"
    mask_end = "MASK_TOT.nii"
    ct_end = "CT.nii"
    descr = 'build a file with two columns which containing path'
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument("input", help="Input top folder")
    parser.add_argument("--adc", help="Ending of ADC files: ADC_1.nii", default=adc_end)
    parser.add_argument("--mask", help="Ending of mask CSI files: MASK_TOT.nii", default=mask_end)
    parser.add_argument("--ct", help="Ending of CT files: CT.nii", default=ct_end)
    parser.add_argument("--name_mask_brain", help="Where you want to save the brain mask", default='MASK_BRAIN.nii')
    parser.add_argument("output", help="Output filename, where you want to save the list")
    return parser

def create_list(folder, ending):
    ADC_files = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(ending):
                full_name = os.path.join(dirpath, filename)
                ADC_files.append(full_name)
    return ADC_files
            
def create_ct_or_mask_paths(adc_list, ending):
    filenames = []
    for filename in adc_list:
        folder_name_list = filename.split(os.sep)[:-2]
        folder_name_list.append(ending)
        filename = os.sep + os.path.join(*folder_name_list)
        filenames.append(filename)
    return filenames

    
def create_txt(filename, mask_list, output_list):
    with open(filename, 'w') as file_:
        for mask, output in zip(mask_list, output_list):
            file_.write("{} {}\n".format(mask, output))

if __name__ == "__main__":
    PARSER = make_parser()
    ARGS = PARSER.parse_args()
    
    ADC = create_list(ARGS.input, ARGS.adc)
    MASK = create_ct_or_mask_paths(ADC, ARGS.mask)
    CT = create_ct_or_mask_paths(ADC, ARGS.ct)
    OUTPUT = create_ct_or_mask_paths(ADC, ARGS.name_mask_brain)
    create_txt(ARGS.output, MASK, OUTPUT)
    
    
    
    
    
    
    
    