'''/home/kurt/PycharmProjects/First/NetworkAutomation/yrender.py'''
#!/usr/bin/env python

import yaml
from jinja2 import Template, Environment, FileSystemLoader
import json

#init var
work_dir = '/home/kurt/NetworkAutomation/NetworkAutomation/datamodel/'
y_file = 'epl_DM2.yml'
j2_file = 'epl2.j2'
js_file = 'inventory.json'
json_data = json.load(open(work_dir + js_file))

#set jinja2 vars
epl_tmpl = Template (open(work_dir + j2_file).read())
env= Environment(loader=FileSystemLoader('.'))

#load yaml and apply jinja2 template
with open(work_dir + y_file, 'r') as y_in:
    print '....rendering yml-data into j2 template....'
    print env.get_template(epl_tmpl).render(yaml.load(y_in), inv_dct = json_data)



