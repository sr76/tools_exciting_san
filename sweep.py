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
    sweeplog = open(resultspath+"/sweep.log","w+")
    sweeplog.write("runspath  "+runspath+"\n")
    sweeplog.write("resultspath  "+resultspath+"\n")
    sweeplog.write("inputtemplatepath  "+inputtemplatepath+"\n")

    inputtree = etree.parse(inputtemplatepath)

    for irun, sweepdic in enumerate(sweepdicarr):
        runpath, rundir = tstamp_folder(runspath)
        os.chdir(runpath)
        sweeplog.write("\n"+"runpath  "+runpath+"\n")

        setinput.setbyxpath(inputtree,"/input/keywords","sdfsdf")

        for xpath,value in sweepdic.items():
            sweeplog.write("\t"+"sweepvar  "+xpath+"\n")
            sweeplog.write("\t"+"value  "+value+"\n")

            setinput.setbyxpath(inputtree,xpath,value)
        
        inputtree.write(runpath+"/input.xml",pretty_print="true")
        
        
    sweeplog.close()

runspath="/home1/srigamonti/projects/cobalt_bulk/runs"
resultspath="/home1/srigamonti/projects/cobalt_bulk/results/sweepkgrid"
inputtemplatepath="/home1/srigamonti/projects/cobalt_bulk/runs/20/input.xml"
sweepdicarr=[]
sweepdicarr.append({"/input/groundstate/@ngridk":"34 34 32"})
sweepdicarr.append({"/input/groundstate/@ngridk":"5 5 27"})


sweep(runspath,resultspath,inputtemplatepath,sweepdicarr)



