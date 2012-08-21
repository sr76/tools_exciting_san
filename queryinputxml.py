import numpy as np
from lxml import etree
import os
import sys


def getByXpath(xpath,fname):
    tree = etree.parse(fname)
    return tree.xpath(xpath)
