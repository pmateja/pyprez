#!/usr/bin/env python
from lxml import etree

class walidacja(object):
    xml = ""
    xsd = ""
    log = ""
    def __init__(self, ml, sl):
        self.pxml(ml)
        self.pxsd(sl)
    def pxml(self, plik):
        try:
            open(plik)
            self.xml = plik    
        except:
            print "Brak pliku"
    def pxsd(self, plik):
        try:
            open(plik)
            self.xsd = plik    
        except:
            print "Brak pliku"
    def walidacja(self):
        xsd_f = open(self.xsd)
        schema = etree.parse(xsd_f)
        sschema = etree.XMLSchema(schema)

        xml_f = open(self.xml)
        doc = etree.parse(xml_f)
        try:
            ddoc = 0
            sschema.assertValid(doc)
            print "Operacja przebiegla pomyslnie!"
        except:
            ddoc = 1
            print "Blad w czasie walidacji:"
            print sschema.error_log
            log = str(sschema.error_log)
        return ddoc

if __name__ == "__main__":
    xsd = "parser.xsd"
    xml = "test.xml"
    a = walidacja()
    a.pxml(xml)
    a.pxsd(xsd)
    a.wal()
