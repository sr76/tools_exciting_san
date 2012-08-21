import time
import os
import sys
import setinputxml
import queryinfoxml
from lxml import etree
import tstamp_folder

def optimize(runpath,resultspath,inputtemplatepath,vararr,ftolerance=1.e-4,xtolerance=1.e-4,itmax=500,runcommandstring):
    optimizelog = open(resultspath+"/optimize.log","w+")
    optimizelog.write("runpath  "+runspath+"\n")
    optimizelog.write("resultspath  "+resultspath+"\n")
    optimizelog.write("inputtemplatepath  "+inputtemplatepath+"\n")
        


def energy(var, data):
    runpath = data[0]
    inputtemplatepath = data[1]
    runcommand = data[2]
    xpath = data[3]
    
    os.chdir(runpath)
    
    inputtree = etree.parse(inputtemplatepath)

    nvar = len(var)

    for i in range(nvar):
        setinputxml.setByXpath(inputtree,xpath[i],str(var[i]))

    inputtree.write(runpath+"/input.xml",pretty_print="true")

    os.chdir(runpath)
    os.system("rm -f info.xml")
    
    os.system(runcommand)
    
    while not os.path.exists("info.xml"):
        time.sleep(1)

    return -queryinfoxml.getLastTotalEnergy()


runpath = tstamp_folder.tstamp_folder("/home1/srigamonti/projects/cobalt_bulk/runs")
resultspath = "/home1/srigamonti/projects/cobalt_bulk/results/optimizeunitcell"


