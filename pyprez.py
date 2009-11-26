#!/usr/bin/env python

from walidacja import *
from parser import *
import os, sys

we = sys.argv[1]
we2 = "parser.xsd"

def start():
    waliduj = walidacja(we, we2)
    if waliduj.walidacja():
        print """Plik wejsciowy jest uszkodzony."""
        return 1
    print "Jest ok"
    return 0

if start() != 0:
    exit()

prezentacja = xml2obj(open(we))
print prezentacja.slajd[0].id
