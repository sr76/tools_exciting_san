import time
import os
import sys
import setinputxml
import queryinfoxml
from lxml import etree
import tstamp_folder
import amoeba

def optimize(runpath,resultspath,inputtemplatepath,vararr,ftolerance=1.e-4,xtolerance=1.e-4,itmax=500,runcommand):
    optimizelog = open(resultspath+"/optimize.log","w+")
    optimizelog.write("runpath  "+runspath+"\n")
    optimizelog.write("resultspath  "+resultspath+"\n")
    optimizelog.write("inputtemplatepath  "+inputtemplatepath+"\n")
    
    optimizelog.write("Variables:\n")
    
    for var in vararr:
        optimizelog.write("xpath: "+var[0]+"\n")
        optimizelog.write("guess: "+str(var[1])+"\n")
        optimizelog.write("scale: "+str(var[2])+"\n")

    guess = []
    scale = []
    data = []
    data.append(runpath)
    data.append(inputtemplatepath)
    data.append(runcommand)
    data.append([])
    for var in vararr:
        data[-1].append(var[0]) # build xpath array
        guess.append(var[1]) # build array of initial guess values for the variables
        scale.append(var[2])
 
    amoeba(guess,scale,energy,ftolerance,xtolerance,itmax,data)

    optimizelog.close()



def energy(var, data):
    runpath = data[0]
    inputtemplatepath = data[1]
    runcommand = data[2]
    xpath = data[3]
    
    os.chdir(runpath)
    os.system("rm -f info.xml")
    
    inputtree = etree.parse(inputtemplatepath)

    nvar = len(var)

    for i in range(nvar):
        setinputxml.setByXpath(inputtree,xpath[i],str(var[i]))

    inputtree.write(runpath+"/input.xml",pretty_print="true")

    
    os.system(runcommand)
    
    while not os.path.exists("info.xml"):
        time.sleep(1)

    return -queryinfoxml.getLastTotalEnergy()


runpath = tstamp_folder.tstamp_folder("/home1/srigamonti/projects/cobalt_bulk/runs")
resultspath = "/home1/srigamonti/projects/cobalt_bulk/results/optimizeunitcell"
inputtemplatepath = "/home1/srigamonti/projects/cobalt_bulk/runs/1345479936227"
vararr = []
vararr.append(["/input/structure/crystal/@scale",4.74,0.05])
vararr.append(["/input/structure/crystal/basevect[3][3]",1.623,0.05])
runcommandstring = "mpi.py 2 12"

optimize(runpath,resultspath,inputtemplatepath,vararr,ftolerance=1.e-4,xtolerance=1.e-4,itmax=500,runcommandstring)

