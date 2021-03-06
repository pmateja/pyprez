#!/usr/bin/env python
from lxml import etree

class prez_walidacja(object):
    xml = ""
    xsd = ""
    def __init__(self, ml, sl):
        self.pxml(ml)
        self.pxsd(sl)
    def pxml(self, plik):
        try:
            open(plik)
            xml = plik    
        except:
            print "Brak pliku"
    def pxsd(self, plik):
        try:
            open(plik)
            xsd = plik    
        except:
            print "Brak pliku"
    def wal(self):
        xsd_f = open(xsd)
        schema = etree.parse(xsd_f)
        sschema = etree.XMLSchema(schema)

        xml_f = open(xml)
        doc = etree.parse(xml_f)
        try:
            ddoc = sschema.assertValid(doc)
            print "Operacja przebiegla pomyslnie!"
        except:
            print "Blad w czasie walidacji:"
            print sschema.error_log



xsd = "parser.xsd"
xml = "test.xml"
if __name__ == "__main__":
    a = prez_walidacja()
    a.pxml(xml)
    a.pxsd(xsd)
    a.wal()
