#!/usr/bin/python
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import sys
from lxml import etree

dostree=etree.parse("dos.xml")

points = dostree.xpath('/dos/totaldos/diagram')[0]
spins = dostree.xpath('/dos/totaldos/diagram//@nspin')
"""
print spins

for spin in spins:
    print int(spin)

sys.exit()
"""
xdata=[]
ydata=[]
legends = []
for spin in spins:
    spin = int(spin)
    points = dostree.xpath('/dos/totaldos/diagram[@nspin="%d"]'%(spin))[0]
    xdata.append([])
    ydata.append([])
    legends.append("spin %d"%(spin))
    for point in points:
        xdata[spin-1].append(point.attrib['e'])
        ydata[spin-1].append(point.attrib['dos'])



#-------------------------------------------------------------------------------
#Plot DOS
 
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

for i in range(len(spins)):
    ax.plot(xdata[i],ydata[i],colors[np.mod(i,7)],label=legends[i])

ax.legend(loc=2)
#ax.legend()

#ax.set_xlim(0.0,54.0)
#ax.set_ylim(0)
#ax.set_xlabel(str.capitalize(labels[0]["xlabel"])+" [eV]")
#ax.set_ylabel(str.capitalize(labels[0]["ylabel"]))

#plt.savefig('PLOT.ps',  orientation='portrait',format='eps')
#plt.savefig('PLOT.png', orientation='portrait',format='png')
plt.show()



