#!/usr/bin/python3

TRACE_FLAG = True
def TRACE(s):
    if TRACE_FLAG:
        print(s)


def isPointer(s:str):
#Dirty hack
    return '*' in s or 'BSTR' in s

def isOutPointer(s:str):
    return isPointer(s) and len([x for x in ('BSTR', 'VARIANT', '**') if x in s]) > 0

def generate_FIXME(paras:list):
    #FIXME: VERY Dirty hack
    ret = "FIXME(\"("
    for i in paras[:-1]:
        if isPointer(i):
            ret += "%p "
        else:
            ret += "%! "
    ret = ret.rstrip()
    ret += ")->("
    ret += ")" + "\\" + "n\", This"
    for i in paras[1:-1]:
        name = i.split(' ')[1].replace('*', '')
        ret += ", " + name
    ret += ");"
    return ret

def get_header(s):
    '''
    All necessary imformation is in header'''
    s = s.replace("FORCEINLINE HRESULT I", "HRESULT WINAPI ")
    s1 = s.replace('This,', 'iface, ')
    header = s1.split('{')[0].rstrip()
    return header

def get_parameter_list(header:str):
    '''
    Returns a list'''
    para = header.split('(')[1].split(')')[0]
    paras = para.split(',')
    return [s.strip() for s in paras]


def single_function(s):
    '''
    Receives a string for a function
    Returns a string for a function'''
    header = get_header(s)
    return header


