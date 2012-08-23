#!/usr/bin/python
import os
import sys
sys.path.append(os.getcwd())
import runlistconfig as rlc # runlistconfig.py should be present in your current working directory for this script to work


"""
# Example of file runlistconfig.py that should be present in your working directory

runlistpath = "/home1/srigamonti/projects/cobalt_bulk/results/sweepnempty/rundir.log"
runcommand = "mpi.py 2 12"

"""
"""
runlistpath: path to a file containing in each line the path to the 
directory where the input.xml (and eventually other needed input files) 
file are for each of the exciting run.

runcommand: the command with which exciting will be run, for example 
"qsub script" or "excitingser > output" or whatever.
"""

def runlist(runlistpath,runcommand):
    runs = open(runlistpath,"r")
    
    for rundir in runs.readlines():
        os.chdir(rundir.rstrip())
        os.system(runcommand)




runlist(rlc.runlistpath,rlc.runcommand)

