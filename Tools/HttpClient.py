#!/usr/bin/env python
# coding:utf8

import json
import cookielib
import urllib2
from socket import socket

class HttpClient(object):

    def __init__(self, proxy=None):
        self.post_data = None
        __cookie = cookielib.CookieJar()
        
        if proxy is None: 
            self.__req = urllib2.build_opener(urllib2.HTTPCookieProcessor(__cookie))
        else:
            self.__proxy_handler = urllib2.ProxyHandler({'http': proxy})
            self.__req = urllib2.build_opener(urllib2.HTTPCookieProcessor(__cookie), __proxy_handler)
            
        urllib2.install_opener(self.__req)
    
    
    def setHeaders(self, headers):
        """
        self.__req.addheaders = [
            ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
            ('User-Agent',
             'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
        ]
        """
        self.__req.addheaders = headers
        urllib2.install_opener(self.__req)


    #@staticmethod
    def doGet(self, url, refer=None):
        print url
        try:
            req = urllib2.Request(url)
            if not (refer is None):
                req.add_header('Referer', refer)
            response = urllib2.urlopen(req)
            html = response.read()
            response.close()
            return html
        except urllib2.HTTPError, e:
            return e.read()
       
    def post_dataToJsonDump(self, post_data):
        self.post_data = json.dumps(post_data)
            
    #@staticmethod        
    def doPost(self, url, post_data, refer=None):
        """
        post_data type is dict
        """
        try:
            if self.post_data is None:
                url = "%s?%s" % (url, urllib.urlencode(post_data))
            else:
                post_data = self.post_data
                
            req = urllib2.Request(url, post_data)
            if not (refer is None):
                req.add_header('Referer', refer)
            response = urllib2.urlopen(req)
            request = response.read()
            response.close()
            return request
        except urllib2.HTTPError, e:
            return e.read()


if __name__ == "__main__":
    http = HttpClient()

    html = http.doGet("http://www.baidu.com")
    print html
