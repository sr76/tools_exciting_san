import time
import os
import sys
import setinput
from lxml import etree

def optimize(runpath,resultspath,inputtemplatepath,varxpatharr,varvaluearr,varscalearr,ftolerance=1.e-4,xtolerance=1.e-4,itmax=500,runcommandstring):
    optimizelog = open(resultspath+"/optimize.log","w+")
    optimizelog.write("runpath  "+runspath+"\n")
    optimizelog.write("resultspath  "+resultspath+"\n")
    optimizelog.write("inputtemplatepath  "+inputtemplatepath+"\n")
    
