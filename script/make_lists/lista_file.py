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
    ct_end = "CT.nii"
    descr = 'build a file with two columns which containing path'
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument("input", help="Input top folder")
    parser.add_argument("--adc", help="Ending of ADC files: ADC_1.nii", default=adc_end)
    parser.add_argument("--ct", help="Ending of CT files: CT.nii", default=ct_end)
    parser.add_argument("output", help="Output filename")
    return parser

def create_list(folder, ending):
    ADC_files = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(ending):
                full_name = os.path.join(dirpath, filename)
                ADC_files.append(full_name)
    return ADC_files
            
def create_ct_paths(adc_list, ending):
    filenames = []
    for filename in adc_list:
        folder_name_list = filename.split(os.sep)[:-2]
        folder_name_list.append(ending)
        filename = os.sep + os.path.join(*folder_name_list)
        filenames.append(filename)
    return filenames

def create_txt(filename, adc_list, ct_list):
    with open(filename, 'w') as file_:
        for adc, ct in zip(adc_list, ct_list):
            file_.write("{} {}\n".format(adc, ct))

if __name__ == "__main__":
    PARSER = make_parser()
    ARGS = PARSER.parse_args()
    
    ADC = create_list(ARGS.input, ARGS.adc)
    CT = create_ct_paths(ADC, ARGS.ct)
    create_txt(ARGS.output, ADC, CT)