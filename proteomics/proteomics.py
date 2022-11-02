#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 16:13:35 2022

@author: davidnoe
"""


# Helper functions
def clean_csv(csv):
    data = csv.readlines()
    data.pop(0)
    return data
    

def extract_protein(line):
    prot_name = str(line).split(',')[0]
    return prot_name


def create_protein_list(file, sort):
    file_clean = clean_csv(file)
    protein_list = []

    for protein in file_clean:
        name = extract_protein(protein)
        protein_list.append(name)

    if sort:
        protein_list.sort()

    return protein_list


def list_overlap(list1, list2, intersecting_values):
    overlap = []
    unique = []
    for value in list1:
        if value in list2:
            overlap.append(value)
        else:
            unique.append(value)
    if intersecting_values:
        return overlap
    # return unique values of first list passed to function
    else:
        return unique


# Plasma
plasma_doc = open('human_plasma_proteins.csv')
plasma_all = create_protein_list(plasma_doc, True)
print('Protein count plasma:', len(plasma_all))
plasma_doc.close()

# Brain
brain_doc = open('human_brain_proteins.csv')
brain_all = create_protein_list(brain_doc, True)
print('Protein count brain:', len(brain_all))
brain_doc.close()

# Filtering
brain_only = list_overlap(brain_all, plasma_all, False)
plasma_only = list_overlap(plasma_all, brain_all, False)
brain_and_plasma = list_overlap(plasma_all, brain_all, True)

print('Number brain only proteins:', len(brain_only))
print('Protein 191 brain:', brain_only[191])
print('Number plasma only proteins:', len(plasma_only))
print('Protein 191 plasma:', plasma_only[191])
print('Number of proteins in brain and plasma:', len(brain_and_plasma))
print('Protein 191 in brain & plasma:', brain_and_plasma[191])




#%%
