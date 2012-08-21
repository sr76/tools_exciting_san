import numpy as np
from lxml import etree
import os
import sys


def getByXpath(xpath,fname):
    tree = etree.parse(fname)
    if "@" in xpath:
        return tree.xpath(xpath)[0]
    else:
        return tree.xpath(xpath)[0].text



xpath = "/input/structure/crystal/basevect[3]"
xpath = "/input/structure/crystal/@scale"
xpath = "/input/structure/crystal/basevect[3]"
fname = "/home1/srigamonti/projects/cobalt_bulk/runs/1345479936227/input.xml"


print getByXpath(xpath,fname)
