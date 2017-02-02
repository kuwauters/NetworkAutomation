#!/usr/bin/env python

import sys
from jinja2 import Environment, FileSystemLoader
import yaml
from pprint import pprint


print 'Reading file ....' + sys.argv[1]
with open(sys.argv[1]) as _: yamldict = yaml.load(_)
print yamldict

print sys.argv[1]
print sys.argv[2]