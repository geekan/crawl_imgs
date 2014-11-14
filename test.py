#!/usr/bin/env python

import os.path
import urllib
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

def retrieve(url, path):
    try:
        print 'retrieve:', url, ' to', path
        if os.path.exists(path):
            return 'file exists:', url, path
        urllib.urlretrieve(url, path)
        ftype = imghdr.what(path)
        if ftype != path.split('.')[-1] and path.split('.')[-1] != 'jpg':
            os.rename(path, path+ftype)
        return 'success:', url, path, ftype
    except Exception as e:
        exception = 'exception: ' + url + ' ' + path + ' | ' + str(e)
        exceptions.append(exception)
        return exception

def main():
    pool = Pool(processes=128)
    exist_file = 0
    socket.setdefaulttimeout(3)
    with open('urls.log') as f:
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
