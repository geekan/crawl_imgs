#!/usr/bin/env python

import urllib

def main():
    with open('urls.log') as f:
        for line in f:
            print line.split()
    # urllib.urlretrieve("http://3gimg.qq.com/wap30/info/info5/img/newshare.png", "2.png")

if __name__ == '__main__':
    main()
