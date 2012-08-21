import numpy as np
from lxml import etree
import os
import sys


def getLastTotalEnergy():
    tree = etree.parse("info.xml")
    return tree.xpath('/info/groundstate/scl/iter[last()]/energies/@totalEnergy')
