#!/usr/bin/python3

TRACE_FLAG = True
def TRACE(s):
    if TRACE_FLAG:
        print(s)

try:
    from config import *
except ImportError:
    print('Load default settings')
    from config_default import *

def isStr(s:str):
    return 'BSTR' in s

def isPointer(s:str):
    return '*' in s

def getParaName(para:str):
    #FIXME: Dirty hack
    name = para.split(' ')[1].replace('*', '')
    if isPointer(para):
        return name
    elif isStr(para):
        return "debugstr_w(" + name + ")"
    elif 'VARIANT' in para:
        return "debugstr_variant(&" + name + ")"
    else:
        return name

def getOutputSymbol(para:str):
    if isPointer(para):
        return "%p"
    elif isStr(para) or 'VARIANT' in para:
        return "%s" #Need more work in getParaName
    elif 'ULONG' in para:
        return "%u"
    elif 'LONG' in para or 'int' in para:
        return "%d"
    else:
        raise NotImplementedError('got ' + para)


def generate_FIXME(paras:list):
    #FIXME: No Robust
    if len(paras) == 0:
        raise RuntimeError("Not a valid parameter list")
    if len(paras) == 1:
        return "FIXME(\"(%p)->()\\n\", This);"
    ret = "FIXME(\"(%p)->("
    for i in paras[1:]:
        ret += getOutputSymbol(i) + " "
    ret = ret.rstrip()

    ret += ")" + "\\" + "n\", This"
    for i in paras[1:-1]:
        ret += ", " + getParaName(i)
    ret += ", " + getParaName(paras[-1]) + ");"
    return ret

def replace_all(s:str, find:str, to:str):
    while find in s:
        s = s.replace(find, to)
    return s

def get_header(s):
    '''
    All necessary imformation is in header'''
    s = s.replace("FORCEINLINE HRESULT I", "HRESULT WINAPI ")
    s1 = s.replace('* This', ' *iface')

#FIXME: Dirty hack for spaces
    s2 = s1.replace(', ', ',')
    s3 = s2.replace(',', ', ')

    header = s3.split('{')[0].rstrip()
    return header

def get_parameter_list(header:str):
    '''
    Returns a list'''
    para = header.split('(')[1].split(')')[0]
    paras = para.split(',')
    return [s.strip() for s in paras]


def single_function(s:str):
    '''
    Receives a string for a function
    Returns a string for a function'''
    header = get_header(s)
    fixme = generate_FIXME(get_parameter_list(header))
    newline = "\n"
    ret = header + newline \
        + '{' + newline \
        + BEFORE_FIXME + newline \
        + INDENT + fixme + newline \
        + INDENT + "return E_NOTIMPL;" + newline \
        + '}' + newline + newline
    return ret

def multiple_functions(s:str):
    data = [i.strip() + '}' for i in s.split('}') if i.strip() != ""]
    outputs = [single_function(i)  for i in data]
    ret = "".join(outputs)
    return ret

if __name__ == '__main__':
    import sys
    try:
        filename = sys.argv[1]
    except IndexError:
        filename = 'input.txt'
    TRACE('Opening file: ' + filename)
    with open(filename, 'r') as fin:
        data = fin.read()
        result = multiple_functions(data)

    try:
        output_filename = sys.argv[2]
    except IndexError:
        TRACE('Use default output filename')
        output_filename = 'output.txt'

    with open(output_filename, 'w') as fout:
        fout.write(result)
