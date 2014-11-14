#!/usr/bin/env python

import urllib
from multiprocessing import Pool

results = []
def callback(result):
    results.append(result)

def main():
    pool = Pool(processes=36)
    with open('urls.log') as f:
        for index, line in enumerate(f):
            try:
                count, url = line.split()
            except:
                print 'exception:', count, url
                continue
            print count, url
            result = pool.apply_async(
                    urllib.urlretrieve,
                    args=(url, 'imgs/'+str(index)+'.'+count+'.'+url.split('/')[-1]),
                    # callback=callback
            )
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()
