#!/usr/bin/python3

TRACE_FLAG = True
def TRACE(s):
    if TRACE_FLAG:
        print(s)

def replace_function_type(s):
    return s.replace("FORCEINLINE HRESULT I", "HRESULT WINAPI ")

def single_function(s):
    '''
    Receives a string for a function
    Returns a string for a function'''

    s1 = replace_function_type(s)
    s1 = s1.replace('This', 'iface')

#All necessary imformation is in header
    header = s1.split('{')[0].rstrip()

