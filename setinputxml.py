from lxml import etree



def setByXpath(inputtree,xpath,value):
    if "@" in xpath:
        element = xpath.split("/@")[0]
        attrib = xpath.split("/@")[1]
        inputtree.xpath(element)[0].attrib[attrib]=value

    else:
        inputtree.xpath(xpath)[0].text = value

