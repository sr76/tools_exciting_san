import numpy as np
from lxml import etree
import os
import sys


def getLastTotalEnergy(fname):
    tree = etree.parse(fname)
    return tree.xpath('/info/groundstate/scl/iter')[-1][0].get("totalEnergy")
