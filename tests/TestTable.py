#format [(parameter, expect) ...]

TABLE_SINGLE_FUNCTION = [
('''static FORCEINLINE HRESULT IHTMLXMLHttpRequest_get_responseXML(IHTMLXMLHttpRequest* This,IDispatch **p) {
    return This->lpVtbl->get_responseXML(This,p);
}''',
'''static HRESULT WINAPI HTMLXMLHttpRequest_get_responseXML(IHTMLXMLHttpRequest* This,IDispatch **p)
{
    HTMLXMLHttpRequest *This = impl_from_IHTMLXMLHttpRequest(iface);
    FIXME("(%p)->(%p)\n", This, p);
    return E_NOTIMPL;
}

''')
]