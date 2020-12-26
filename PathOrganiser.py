# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 15:34:39 2020

@author: shrir
"""


import os
from pathlib import Path
downloads = 'D:/Projects/trial/' 
downloads = input("Enter Path To Organise: ")
downloads.replace(os.sep, '/')
if not downloads.endswith('/'):
    downloads=downloads+'/'
while not os.path.exists(downloads):
    print("\nCould not Identify Path")
    downloads = input("Enter Path To Organise: ")
    downloads.replace(os.sep, '/')
    if not downloads.endswith('/'):
        downloads=downloads+'/'
if not os.path.exists(downloads+'Images'):
    os.makedirs(downloads+'Images')
if not os.path.exists(downloads+'Documents'):
    os.makedirs(downloads+'Documents')
if not os.path.exists(downloads+'Music'):
    os.makedirs(downloads+'Music')
if not os.path.exists(downloads+'Videos'):
    os.makedirs(downloads+'Videos')
if not os.path.exists(downloads+'Compressed'):
    os.makedirs(downloads+'Compressed')
if not os.path.exists(downloads+'Programming Stuff'):
    os.makedirs(downloads+'Programming Stuff')
if not os.path.exists(downloads+'Executables'):
    os.makedirs(downloads+'Executables')

cntr=0
print("\n")
for files in os.listdir(downloads):
    if not os.path.isfile(downloads+files):
        continue
    print("Moving "+files)
    if files.endswith(('.jfif','.jpeg','.jpg','.png','.gif','.webp','.tiff','.psd','.raw','.bmp','.heif','.indd','.jpeg 2000')):
        Path(downloads+files).rename(downloads+'Images/'+files)
        cntr+=1
        continue
    elif files.endswith(('.doc','.docx','.html','.htm','.odt','.pdf','.xls','.xlsx','.ods','.ppt','.pptx','.txt')):
        Path(downloads+files).rename(downloads+'Documents/'+files)
        cntr+=1
        continue
    elif files.endswith(('.aif','.cda','.mid','.midi','.mp3','.mpa','.ogg','.wav','.wma','.wpl')):
        Path(downloads+files).rename(downloads+'Music/'+files)
        cntr+=1
        continue
    elif files.endswith(('mp4','avi','mov','flv','wmv')):
        Path(downloads+files).rename(downloads+'Videos/'+files)
        cntr+=1
        continue
    elif files.endswith(('.7z','.arj','.deb','.pkg','.rar','.rpm','.tar.gz','.z','.zip')):
        Path(downloads+files).rename(downloads+'Compressed/'+files)
        cntr+=1
        continue
    elif files.endswith(('.c','.cpp','.py','.htm','.html','.java')):
        Path(downloads+files).rename(downloads+'Programming Stuff/'+files)
        cntr+=1
        continue
    elif files.endswith(('.exe','.bat','.msi','.apk')):
        Path(downloads+files).rename(downloads+'Executables/'+files)
        cntr+=1
        continue
    else:
        print("Could not identify "+files)
print("\n\nOrganised Successfully!")
print("Total Files Moved: "+str(cntr))
        
