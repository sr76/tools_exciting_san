import os


def runlist(runlistpath,runcommand):
    runs = open(runlistpath,"r")
    
    for rundir in runs.readlines():
        os.chdir(rundir.rstrip())
        os.system(runcommand)




#runlistpath = "/home1/srigamonti/projects/cobalt_bulk/results/sweeprgkmax/rundir.log"
runlistpath = "/home1/srigamonti/projects/cobalt_bulk/results/sweepnempty/rundir.log"
runcommand = "mpi.py 2 12"
runlist(runlistpath,runcommand)

