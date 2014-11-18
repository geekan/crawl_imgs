#!/usr/bin/env python

import os
import os.path
import urllib
import urllib2
import socket
import imghdr
from multiprocessing import Pool
from urlparse import urlparse

results = []
exceptions = []
def callback(result):
    print 'result:', result
    if result:
        results.append(result)

def path_exists(path):
    fname = path.split('/')[-1]
    for exist_fname in files:
        if exist_fname.startswith(fname):
            return exist_fname
    return False

def retrieve(url, path):
    try:
        print 'retrieve:', url, ' to', path
        if os.path.exists(path):
            return 'file exists:', url, path
        elif path_exists(path):
            return 'similar file:', url, path

        # urllib.urlretrieve(url, path)

        headers = {
            "Proxy-Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.6 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,sk;q=0.4",
            "If-Modified-Since": "Wed, 06 Aug 2008 23:37:00 GM",
        }
        req = urllib2.Request(url)
        binary = urllib2.urlopen(req).read()
        with open(path, 'w') as f:
            f.write(binary)

        ftype = imghdr.what(path)
        if ftype and ftype != path.split('.')[-1] and path.split('.')[-1] != 'jpg':
            os.rename(path, path+'.'+ftype)
        elif ftype is None:
            os.rename(path, path+'.none')
        return 'success:', url, path, ftype
    except Exception as e:
        exception = 'exception: ' + url + ' ' + path + ' | ' + str(e)
        exceptions.append(exception)
        return exception

# Use Proxifier or other global proxy for dynamic proxy
def build_proxy():
    hk_proxy = urllib2.ProxyHandler({'https': 'web-proxyhk.oa.com:8080', 'http': 'web-proxyhk.oa.com:8080'})
    hk_opener = urllib2.build_opener(hk_proxy)
    urllib2.install_opener(hk_opener)

files = os.listdir('./imgs')
def main():
    #build_proxy()
    pool = Pool(processes=128)
    exist_file = 0
    socket.setdefaulttimeout(3)
    with open('samples.log') as f:
        for index, line in enumerate(f):
            try:
                count, url = line.split()
            except:
                print 'exception:', count, url
                continue

            # print 'main:', count, url
            fname = urlparse(url).path.split('/')[-1]
            path = './imgs/'+str(index)+'.'+count+'.'+fname

            result = pool.apply_async(
                    retrieve,
                    args=(url, path),
                    callback=callback
            )
        print 'apply async done'
    pool.close()
    pool.join()
    for e in exceptions:
        print e

if __name__ == '__main__':
    main()
