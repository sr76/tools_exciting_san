import numpy as np
from lxml import etree
import os
import sys


def parseinfoxml(path):
    tree=etree.parse(path+"info.xml")
    labels[i]["xlabel"] = tree.xpath('/info/groundstate/scl/iter/energies')[0].attrib["totalEnergy"]



scwd = str(os.getcwd())
parseinfoxml(scwd)
