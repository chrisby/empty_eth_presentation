from glob import glob 
from os.path import join, dirname, basename
from os import makedirs
import os
from shutil import copyfile

for t in glob('/Volumes/bs-dfs/group/borgwardt/Projects/KDD2019_Meaningless_Time_Series_Kernels/Data/UCR/**/*TEST'):
    fol = basename(dirname(t))
    makedirs(f'./UCR/{fol}', exist_ok=True)
    file_name = basename(t)
    copyfile(t, f'./UCR/{fol}/{file_name}')

for t in glob('/Volumes/bs-dfs/group/borgwardt/Projects/KDD2019_Meaningless_Time_Series_Kernels/Data/UCR/**/*TRAIN'):
    fol = basename(dirname(t))
    makedirs(f'./UCR/{fol}', exist_ok=True)
    file_name = basename(t)
    copyfile(t, f'./UCR/{fol}/{file_name}')
