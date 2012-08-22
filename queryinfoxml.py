import numpy as np
from lxml import etree
import os
import sys


def getLastTotalEnergy():
    tree = etree.parse("info.xml")
    return float(tree.xpath('/info/groundstate/scl/iter[last()]/energies/@totalEnergy'))


"""
# Just for testing purposes

inputtree = etree.parse("/home1/srigamonti/projects/cobalt_bulk/runs/1345479936227/input.xml")

xpath = "/input/structure/crystal/basevect[3][3]"

value = "Keywords for the run"

setByXpath(inputtree,xpath,value)

#inputtree.write("input.xml",pretty_print="true")
print etree.tostring(inputtree)
"""
