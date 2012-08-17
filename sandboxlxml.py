from lxml import etree

fname="/home1/srigamonti/projects/cobalt_bulk/runs/20/input.xml"

tree = etree.parse(fname)
root = tree.getroot()

print root.xpath('/input/groundstate/@ngridk')
print root.xpath('/input/structure/crystal/basevect[3]/text()')
print len(root)
print tree.xpath('/input/groundstate/@ngridk')


"""
tree.xpath('/input/groundstate')[0].attrib['ngridk']="hola"
print tree.xpath('/input/groundstate/@ngridk')

print tree.xpath('/input/structure/crystal/basevect[3]/text()')
tree.xpath('/input/structure/crystal/basevect[3]')

tree.xpath('/input/groundstate')[0].attrib['ngridk']="hola"
print tree.xpath('/input/groundstate')[0].attrib['ngridk']
print tree.xpath('/input/groundstate/@ngridk')
print tree.xpath('/input/groundstate/@rgkmax')
print tree.xpath('/input/structure/crystal/basevect[3]/text()')
"""

print etree.tostring(tree)


