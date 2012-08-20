import time
import os
import sys
import setinput
from lxml import etree


def tstamp_folder(rpath):
    sstamp = str(int(time.time()*1000))
    if rpath[-1]!="/":
        rpath=rpath+"/"
    os.system("mkdir %s"%(rpath+sstamp))
    return rpath+sstamp,sstamp


def sweep(runspath,resultspath,inputtemplatepath,sweepdicarr):

    inputtree = etree.parse(inputtemplatepath)

    for irun, sweepdic in enumerate(sweepdicarr):
        runpath, rundir = tstamp_folder(runspath)
        os.chdir(runpath)

        for xpath,value in sweepdic.items():
            setinput.setbyxpath(inputtree,xpath,value):
            


runspath="/home1/srigamonti/projects/cobalt_bulk/runs"
resultspath="/home1/srigamonti/projects/cobalt_bulk/results/sweepkgrid"
inputtemplatespath="/home1/srigamonti/projects/cobalt_bulk/results/sweepkgrid/input.xml"
sweepdicarr=[]
sweepdicarr.append({"/input/groundstate/@ngridk":"34 34 32"})
sweepdicarr.append({"/input/groundstate/@ngridk":"5 5 27"})


sweep(runspath,resultspath,inputtemplatepath,sweepdicarr)



