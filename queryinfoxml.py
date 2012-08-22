import numpy as np
from lxml import etree
import os
import sys


def getLastTotalEnergy():
    tree = etree.parse("info.xml")
    return float(tree.xpath('/info/groundstate/scl/iter[last()]/energies/@totalEnergy')[0])


"""
# Just for testing purposes

infopath = "/home1/srigamonti/projects/cobalt_bulk/runs/1345479936227/"
os.chdir(infopath)

print getLastTotalEnergy()
"""
