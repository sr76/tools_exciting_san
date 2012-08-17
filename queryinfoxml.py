import numpy as np
from lxml import etree
import os
import sys


def parseinfoxml(path):
    tree = etree.parse(path+"/info.xml")
    iter = tree.xpath('/info/groundstate/scl/iter')
    print iter[-1][0].get("totalEnergy")


scwd = str(os.getcwd())
parseinfoxml(scwd)
