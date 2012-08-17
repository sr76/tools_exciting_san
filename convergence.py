import time
import os
import sys

def tstamp_folder(rpath):
    sstamp = str(int(time.time()*1000))
    if rpath[-1]!="/":
        rpath=rpath+"/"
    os.system("mkdir %s"%(rpath+sstamp))
    return rpath+sstamp,sstamp


def sweepandwatch(runspath,resultspath,sweepxpatharr,watchxpatharr,inputtemplatepath,sweepvaluesarr):
    for i,sweepvalue in enumerate(sweepvaluesarr):
        runpath, rundir = tstamp_folder(runspath)
        os.chdir(runpath)
        

