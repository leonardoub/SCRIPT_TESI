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
    parser.add_argument("folder_path_output_extracion", help="Where you want to save the result of extraction of features")
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
            
def create_ct_paths(adc_list, ending):
    filenames = []
    for filename in adc_list:
        folder_name_list = filename.split(os.sep)[:-2]
        folder_name_list.append(ending)
        filename = os.sep + os.path.join(*folder_name_list)
        filenames.append(filename)
    return filenames

def create_output_list_path(adc_list, folder_path_extraction):
    output_list_path = []
    for filename in adc_list:
        folder_patient = filename.split(os.sep)[-3]
        full_path_output = os.path.join(folder_path_extraction, folder_patient + '.csv')
        output_list_path.append(full_path_output)
    return output_list_path
        

def create_txt(filename, adc_list, ct_list, output_list):
    with open(filename, 'w') as file_:
        for adc, ct, output in zip(adc_list, ct_list, output_list):
            file_.write("{} {} {}\n".format(adc, ct, output))

if __name__ == "__main__":
    PARSER = make_parser()
    ARGS = PARSER.parse_args()
    
    ADC = create_list(ARGS.input, ARGS.adc)
    CT = create_ct_paths(ADC, ARGS.ct)
    OUTPUT = create_output_list_path(ADC, ARGS.folder_path_output_extracion)
    create_txt(ARGS.output, ADC, CT, OUTPUT)