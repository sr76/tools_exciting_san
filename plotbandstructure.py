#!/usr/bin/python
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import sys
from lxml import etree

bandstree=etree.parse("bandstructure.xml")

bands = bandstree.xpath('/bandstructure/band')
nbands = len(bands)

xdata=[]
ydata=[]
legends = []
for band in bands:
    xdata.append(band.xpath("point/@distance"))
    ydata.append(band.xpath("point/@eval"))


#convert the data from strings to floats
for band in range(nbands):
    for i,x in enumerate(xdata[band]):
        xdata[band][i]=float(xdata[band][i])
    for i,x in enumerate(ydata[band]):
        ydata[band][i]=float(ydata[band][i])


#-------------------------------------------------------------------------------
#Plot BANDS
 
#colors=['k','r','g','b','y','c','m']
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

for band in range(nbands):
    ax.plot(xdata[band],ydata[band],'k')

ax.legend(loc=2)
#ax.legend()

#ax.set_xlim(0.0,54.0)
#ax.set_ylim(0)
#ax.set_xlabel(str.capitalize(labels[0]["xlabel"])+" [eV]")
#ax.set_ylabel(str.capitalize(labels[0]["ylabel"]))

#plt.savefig('PLOT.ps',  orientation='portrait',format='eps')
#plt.savefig('PLOT.png', orientation='portrait',format='png')
plt.show()


