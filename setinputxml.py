from lxml import etree


"""
# Example of use:

from lxml import etree

inputtree = etree.parse("input.xml")
xpath = "/input/groundstate/@nempty"
value = 5

setinputxml.setByXpath(inputtree,xpath,value)

inputtree.write("input.xml",pretty_print="true")

# Another example of use:

from lxml import etree

inputtree = etree.parse("input.xml")
xpath = "/input/keywords" # or equivalently "/input/keywords[1]"
value = "Keywords for the run"

setinputxml.setByXpath(inputtree,xpath,value)

inputtree.write("input.xml",pretty_print="true")

# Example of xpath to change the third basevect of the crystal structure definition:

from lxml import etree

inputtree = etree.parse("input.xml")
xpath = "/input/structure/crystal/basevect[3]" # or equivalently "/input/keywords[1]"
value = "Keywords for the run"

setinputxml.setByXpath(inputtree,xpath,value)

inputtree.write("input.xml",pretty_print="true")

"""


def setByXpath(inputtree,xpath,value):
    if "@" in xpath:
        element = xpath.split("/@")[0]
        attrib = xpath.split("/@")[1]
        inputtree.xpath(element)[0].attrib[attrib]=value

    else:
        if "][" in xpath:
            # In this case, the xpath is something like
            # /input/structure/crystal/basevect[3][3]
            # where we want to address the third component of the third basevect vector.
            basexpath = xpath.split("][")[-2]+"]"
            oldtext = inputtree.xpath(basexpath)[0].text
            stext = oldtext.split()
            component = int(xpath.split("][")[1][:-1])
            stext[component-1] = str(value)
            newtext = "  ".join(stext)
            inputtree.xpath(basexpath)[0].text = newtext
        else:
            inputtree.xpath(xpath)[0].text = value


"""
inputtree = etree.parse("/home1/srigamonti/projects/cobalt_bulk/runs/1345479936227/input.xml")

xpath = "/input/structure/crystal/basevect[3][3]"

value = "Keywords for the run"

setByXpath(inputtree,xpath,value)

#inputtree.write("input.xml",pretty_print="true")
print etree.tostring(inputtree)
"""
