import time
import os


def tstamp_folder(rpath):
    sstamp = str(int(time.time()*1000))
    if rpath[-1]!="/":
        rpath=rpath+"/"
    os.system("mkdir %s"%(rpath+sstamp))
    return rpath+sstamp,sstamp

