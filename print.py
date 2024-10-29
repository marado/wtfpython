#!/usr/bin/python3
import sys
import xml.dom.minidom
test = xml.dom.minidom.parse(sys.argv[1])
test.writexml(sys.stdout, indent='', addindent='  ', newl='\n', encoding="UTF-8")
