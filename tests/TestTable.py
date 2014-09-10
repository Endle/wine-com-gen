#format [(parameter, expect) ...]

TABLE_MULTIPLE_FUNCTIONS = [
('''static FORCEINLINE HRESULT IHTMLXMLHttpRequest_get_responseXML(IHTMLXMLHttpRequest* This,IDispatch **p) {
    return This->lpVtbl->get_responseXML(This,p);
}
static FORCEINLINE HRESULT IHTMLXMLHttpRequest_get_responseXML(IHTMLXMLHttpRequest* This,IDispatch **p) {
    return This->lpVtbl->get_responseXML(This,p);
}''',
'''static HRESULT WINAPI HTMLXMLHttpRequest_get_responseXML(IHTMLXMLHttpRequest *iface, IDispatch **p)
{
    HTMLXMLHttpRequest *This = impl_from_IHTMLXMLHttpRequest(iface);
    FIXME("(%p)->(%p)\\n", This, p);
    return E_NOTIMPL;
}

static HRESULT WINAPI HTMLXMLHttpRequest_get_responseXML(IHTMLXMLHttpRequest *iface, IDispatch **p)
{
    HTMLXMLHttpRequest *This = impl_from_IHTMLXMLHttpRequest(iface);
    FIXME("(%p)->(%p)\\n", This, p);
    return E_NOTIMPL;
}

''')
]
TABLE_SINGLE_FUNCTION = [
('''static FORCEINLINE HRESULT IHTMLXMLHttpRequest_get_responseXML(IHTMLXMLHttpRequest* This,IDispatch **p) {
    return This->lpVtbl->get_responseXML(This,p);
}''',
'''static HRESULT WINAPI HTMLXMLHttpRequest_get_responseXML(IHTMLXMLHttpRequest *iface, IDispatch **p)
{
    HTMLXMLHttpRequest *This = impl_from_IHTMLXMLHttpRequest(iface);
    FIXME("(%p)->(%p)\\n", This, p);
    return E_NOTIMPL;
}

'''),
('''static FORCEINLINE HRESULT IHTMLXMLHttpRequest_get_responseXML(IHTMLXMLHttpRequest* This,BSTR *p) {
    return This->lpVtbl->get_responseXML(This,p);
}''',
'''static HRESULT WINAPI HTMLXMLHttpRequest_get_responseXML(IHTMLXMLHttpRequest *iface, BSTR *p)
{
    HTMLXMLHttpRequest *This = impl_from_IHTMLXMLHttpRequest(iface);
    FIXME("(%p)->(%p)\\n", This, p);
    return E_NOTIMPL;
}

'''),
('''static FORCEINLINE HRESULT IHTMLXMLHttpRequest_setRequestHeader(IHTMLXMLHttpRequest* This,BSTR bstrHeader,BSTR bstrValue) {
    return This->lpVtbl->setRequestHeader(This,bstrHeader,bstrValue);
}''',
'''static HRESULT WINAPI HTMLXMLHttpRequest_setRequestHeader(IHTMLXMLHttpRequest *iface, BSTR bstrHeader, BSTR bstrValue)
{
    HTMLXMLHttpRequest *This = impl_from_IHTMLXMLHttpRequest(iface);
    FIXME("(%p)->(%s %s)\\n", This, debugstr_w(bstrHeader), debugstr_w(bstrValue));
    return E_NOTIMPL;
}

'''),
('''static FORCEINLINE HRESULT IHTMLXMLHttpRequest_abort(IHTMLXMLHttpRequest* This) {
    return This->lpVtbl->abort(This);
}''',
'''static HRESULT WINAPI HTMLXMLHttpRequest_abort(IHTMLXMLHttpRequest *iface)
{
    HTMLXMLHttpRequest *This = impl_from_IHTMLXMLHttpRequest(iface);
    FIXME("(%p)->()\\n", This);
    return E_NOTIMPL;
}

''')
]

TABLE_GET_HEADER = [
('''static FORCEINLINE HRESULT IHTMLXMLHttpRequest_get_responseXML(IHTMLXMLHttpRequest* This,IDispatch **p) {
    return This->lpVtbl->get_responseXML(This,p);
}''',
'static HRESULT WINAPI HTMLXMLHttpRequest_get_responseXML(IHTMLXMLHttpRequest *iface, IDispatch **p)')
]

TABLE_GET_PARAMETER_LIST = [
('static HRESULT WINAPI HTMLXMLHttpRequest_get_responseXML(IHTMLXMLHttpRequest *iface, IDispatch **p)',
['IHTMLXMLHttpRequest *iface', 'IDispatch **p'])
]

TABLE_GENERATE_FIXME = [
(['IHTMLXMLHttpRequest *iface', 'IDispatch **p'],
'FIXME("(%p)->(%p)\\n", This, p);'),
(['IHTMLTable2 *iface', 'LONG indexFrom', 'LONG indexTo', 'IDispatch **row'],
'FIXME("(%p)->(%d %d %p)\\n", This, indexFrom, indexTo, row);'),
(['IHTMLTable2 *iface'],
'FIXME("(%p)->()\\n", This);'),
(['IHTMLTable3 *iface', 'BSTR v'],
'FIXME("(%p)->(%s)\\n", This, debugstr_w(v));'),
(['IHTMLTable *iface', 'VARIANT v'],
'FIXME("(%p)->(%s)\\n", This, debugstr_variant(&v));')
]
