from peers.lib.modules import base

def validated(r, **kwds):
    port = r.environ['SERVER_PORT']
    if port and (port!=80):
        port = ':%s' % port
    
    # check REQUEST_METHOD
    
    # check HTTP_REFERER
    if 'REFERER' not in r.headers:
        return False
    referer = r.headers['REFERER']
    if 'url' in kwds:
        if referer.partition('//')[2].strip('/') != ('%s%s/%s' %
            (r.environ['SERVER_NAME'], port, kwds['url']) ):
            return False
    return True