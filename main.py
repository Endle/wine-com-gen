#!/usr/bin/python3

TRACE_FLAG = True
def TRACE(s):
    if TRACE_FLAG:
        print(s)

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


