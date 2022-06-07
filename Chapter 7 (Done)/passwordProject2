#! python3
# passwordProject2.py - List version of passwordProject.py 

import re, sys

def strong(passw):
    length = re.compile('(\w{8})')
    number = re.compile('(\d)+')
    lower = re.compile('([a-z]+)')
    upper = re.compile('([A-Z]+)')
    list = [length, number, lower, upper]
    
    try:
        for i in list:
            all = i.search(passw)
            all.group()
    except AttributeError:
        print(passw, ':\n'
       """doesn't have 8 characters or more, at least one uppercase
and one lowercase letter, and 1 number or more""")
        sys.exit()
        
    print(passw, 'is a valid password')

strong('caRlindehouse3')
    

