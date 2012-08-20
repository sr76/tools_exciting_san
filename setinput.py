from lxml import etree



def setbyxpath(inputtree,xpath,value):
    print etree.tostring(inputtree)

    if "@" in xpath:
        element = xpath.split("/@")[0]
        attrib = xpath.split("/@")[1]
        inputtree.xpath(element)[0].attrib[attrib]=value

    print etree.tostring(inputtree)
    print "==============================================" 
    print "==============================================" 
    print "==============================================" 
    print "==============================================" 
    
