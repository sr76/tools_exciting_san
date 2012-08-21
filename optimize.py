import time
import os
import sys
import setinput
from lxml import etree

def optimize(runpath,resultspath,inputtemplatepath,vararr,ftolerance=1.e-4,xtolerance=1.e-4,itmax=500,runcommandstring):
    optimizelog = open(resultspath+"/optimize.log","w+")
    optimizelog.write("runpath  "+runspath+"\n")
    optimizelog.write("resultspath  "+resultspath+"\n")
    optimizelog.write("inputtemplatepath  "+inputtemplatepath+"\n")
    


def energy(var, data):
    runpath = data[0]
    inputtemplatepath = data[1]
    runcommand = data[2]
