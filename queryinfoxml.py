import numpy as np
from lxml import etree
import os
import sys


def getLastTotalEnergy(fname):
    tree = etree.parse(fname)
    return tree.xpath('/info/groundstate/scl/iter[last()]/energies/@totalEnergy')
