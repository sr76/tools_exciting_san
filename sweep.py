#!/usr/bin/python

import os
import sys
import setinputxml
from lxml import etree
import tstamp_folder
import time
sys.path.append(os.getcwd())
import sweepconfig # sweepconfig.py should be present in your current working directory for this script to work


"""
# Find below an example of the contents of sweepconfig.py

runspath="/home1/srigamonti/projects/cobalt_bulk/runs"
resultspath="/home1/srigamonti/projects/cobalt_bulk/results/sweepnempty"
inputtemplatepath="/home1/srigamonti/projects/cobalt_bulk/runs/1345479936277/input.xml"
sweepdicarr=[]
sweepdicarr.append({"/input/groundstate/@nempty":"1"})
sweepdicarr.append({"/input/groundstate/@nempty":"2"})
sweepdicarr.append({"/input/groundstate/@nempty":"3"})
sweepdicarr.append({"/input/groundstate/@nempty":"4"})
sweepdicarr.append({"/input/groundstate/@nempty":"5"})
sweepdicarr.append({"/input/groundstate/@nempty":"6"})
sweepdicarr.append({"/input/groundstate/@nempty":"7"})
sweepdicarr.append({"/input/groundstate/@nempty":"8"})
sweepdicarr.append({"/input/groundstate/@nempty":"9"})
sweepdicarr.append({"/input/groundstate/@nempty":"10"})

"""

def sweep(runspath,resultspath,inputtemplatepath,sweepdicarr):
    sweeplog = open(resultspath+"/sweep.log","w+")
    sweeplog.write("runspath  "+runspath+"\n")
    sweeplog.write("resultspath  "+resultspath+"\n")
    sweeplog.write("inputtemplatepath  "+inputtemplatepath+"\n")
    
    rundirlog = open(resultspath+"/rundir.log","w+")
   
   
    inputtree = etree.parse(inputtemplatepath)

    for irun, sweepdic in enumerate(sweepdicarr):
        time.sleep(1)
        runpath, rundir = tstamp_folder.tstamp_folder(runspath)
        os.chdir(runpath)
        sweeplog.write("\n"+"runpath  "+runpath+"\n")
        rundirlog.write(runpath+"\n")

        inputdscr="Input file generated by sweep.py script\n"
        inputdscr=inputdscr+"input.xml template in: %s\n"%(inputtemplatepath)
        inputdscr=inputdscr+"results path is: %s\n"%(resultspath)


        for xpath,value in sweepdic.items():
            sweeplog.write("\t"+"sweepvar  "+xpath+"\n")
            sweeplog.write("\t"+"value  "+value+"\n")

            inputdscr=inputdscr+"sweeping variable: "+xpath+"\n"
            inputdscr=inputdscr+"value: "+value+"\n"
            
            setinputxml.setByXpath(inputtree,xpath,value)
        
        setinputxml.setByXpath(inputtree,"/input/keywords",inputdscr)

        inputtree.write(runpath+"/input.xml",pretty_print="true")
        
        
    sweeplog.close()
    rundirlog.close()


sweep(runspath,resultspath,inputtemplatepath,sweepdicarr)



