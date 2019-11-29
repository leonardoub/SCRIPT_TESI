#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 23:05:26 2019

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
    
    bval_file = "-a.bval"
    bvec_file = "-a.bvec"
    json_file ='-a.json'
    descr = 'build a file with three columns which containing path'
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument("input", help="Input top folder")
    parser.add_argument("--bval", help="Ending of bval files", default=bval_file)
    parser.add_argument("--bvec", help="Ending of bvec files", default=bvec_file)
    parser.add_argument("--json", help="Ending of json files", default=json_file)
    parser.add_argument("output", help="Output filename")
    return parser

def create_list(folder, ending):
    val_files = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(ending):
                full_name = os.path.join(dirpath, filename)
                val_files.append(full_name)
    return val_files

            
#def create_ct_paths(adc_list, ending):
#    filenames = []
#    for filename in adc_list:
#        folder_name_list = filename.split(os.sep)[:-2]
#        folder_name_list.append(ending)
#        filename = os.sep + os.path.join(*folder_name_list)
#        filenames.append(filename)
#    return filenames

def create_txt(filename, bval_list, bvec_list, json_list):
    with open(filename, 'w') as file_:
        for bval, bvec, json_ in zip(bval_list, bvec_list, json_list):
            file_.write("{} {} {}\n".format(bval, bvec, json_)




    PARSER = make_parser()
    ARGS = PARSER.parse_args()
    
    BVAL = create_list(ARGS.input, ARGS.bval)
    BVEC = create_list(ARGS.input, ARGS.bvec)
    JSON = create_list(ARGS.input, ARGS.json)
    create_txt(ARGS.output, BVAL, BVEC, JSON)
