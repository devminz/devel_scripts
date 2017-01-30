#!/usr/bin/python3  
import sys 
import subprocess
import os
import shlex 
import config



filenames = set()
for root, dirs, files in os.walk(config.gitignore_repo):
    for file in files:
        for pat in sys.argv:
            if pat in file and '.gitignore' in file:
                filename = os.path.join(root, file)
                filenames.add(filename)
                print(filename)
                

gitignore_file = os.path.join(os.getcwd(), ".gitignore")

with open(gitignore_file, "ab") as outfile:
    for f in filenames:
         outfile.write(
                 bytes(
                     "\n############ --- {} ##\n".format(os.path.basename(f)),
                     'utf-8')
                 )
         with open(f, "rb") as infile:
             outfile.write(infile.read())




                 

                 
                                     


