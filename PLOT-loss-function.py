#!/usr/bin/python
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from lxml import etree
import os
import sys


#-------------------------------------------------------------------------------
#Check arguments
nfiles=len(sys.argv)-1
if nfiles<1:
    print "\nNothing to plot\n\n*** Usage: ***\n $>PLOT-lossfkt.py path_to_loss_file1.xml path_to_loss_file2.xml ...\n**************\n"
    sys.exit()

fnames=[]
for i in range(nfiles):
    fnames.append(sys.argv[i+1])
    if not os.path.isfile(fnames[i]):
        print "Error: file \"%s\" doesn't exist"%(fnames[i])
        sys.exit()
#-------------------------------------------------------------------------------
#Parse LOSS function data files
xdata=[]
ydata=[]
labels=[]
legends=[]
function=1
for i,fname in enumerate(fnames):
    xdata.append([])
    ydata.append([])
    labels.append({})
    print "Parsing "+fname
    sfname = fname.split("/")[-1].split("_")
    if "FXCRPA" in sfname: legend="RPA "
    if "FXCALDA" in sfname: legend="ALDA "
    if not "NLF" in sfname: legend=legend+"(LFE) "
    if "NLF" in sfname: legend=legend+"(no-LFE) "
    if sfname[-2][0:2]=="OC": legend=legend+"Optical(%s)"%(sfname[-2][2:])
    legends.append(legend)
    tree=etree.parse(fname)
    if "LOSS" in sfname: rootelement="loss"
    if "EPSILON" in sfname: rootelement="dielectric"
    labels[i]["xlabel"] = tree.xpath('/%s/mapdef/variable1'%(rootelement))[0].attrib["name"]
    labels[i]["ylabel"] = tree.xpath('/%s/mapdef/function%d'%(rootelement,function))[0].attrib["name"]

    for elem in tree.xpath('/%s/map'%(rootelement)):
        xdata[i].append(float(elem.attrib["variable1"]))
        ydata[i].append(float(elem.attrib["function%d"%(function)]))

#-------------------------------------------------------------------------------
#Plot LOSS function/s 
colors=['k','r','g','b','y','c','m']
fig=plt.figure(1,figsize=(8,5.5))

params = {'font.size':15,
          'xtick.major.size': 5,
          'ytick.major.size': 5,
          'patch.linewidth': 1.5,
          'axes.linewidth': 2.,
          'axes.formatter.limits': (-4, 6),
          'lines.linewidth': 1.8,
          'lines.markeredgewidth':2.0,
          'lines.markersize':18,
          'legend.fontsize':11,
          'legend.borderaxespad':1,
          'legend.borderpad':0.5,
          'savefig.dpi':80}

plt.rcParams.update(params)

ax=fig.add_subplot(111)

for i in range(nfiles):
    ax.plot(xdata[i],ydata[i],colors[np.mod(i,7)],label=legends[i])

ax.legend(loc=2)
#ax.legend()

ax.set_xlim(0.0,54.0)
ax.set_ylim(0)
ax.set_xlabel(str.capitalize(labels[0]["xlabel"])+" [eV]")
ax.set_ylabel(str.capitalize(labels[0]["ylabel"]))

plt.savefig('PLOT.ps',  orientation='portrait',format='eps')
plt.savefig('PLOT.png', orientation='portrait',format='png')
plt.show()
