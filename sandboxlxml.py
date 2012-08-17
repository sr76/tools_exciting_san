from lxml import etree

fname="/home1/srigamonti/projects/cobalt_bulk/runs/20/info.xml"

tree = etree.parse(fname)
print tree.xpath('/info/groundstate/scl/iter')[-1][0].get("totalEnergy")
print tree.xpath('/info/groundstate/scl/iter')[-1]
