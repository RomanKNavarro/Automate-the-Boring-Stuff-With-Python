#! python3
# passwordProject.py - A Practice Project that determines if an inputted password is "strong" enough

import re

def strong(passw):
    length = re.compile('(\w{8})')
    number = re.compile('(\d)+')
    lower = re.compile('([a-z]+)')
    upper = re.compile('([A-Z]+)')

    l = length.search(passw)
    n = number.search(passw)
    lo = lower.search(passw)
    up = upper.search(passw)
    try:
        print(l.group() + ': Your password has 8 characters or more')
        print(n.group() + ': Your password has number')
        print(lo.group() + ': Your password has lowercase')
        print(up.group() + ': Your password has uppercase')
    except AttributeError:
        print('''\tYour password is invalid. It must contain 8 characters or more,
        have at least one uppercase and one lowercase letter, and at least one number''')
    
strong('fds4')                                                                                                                                              

    
    


    
    
    
