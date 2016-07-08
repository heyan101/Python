#!/usr/bin/env python
# coding:utf8


from HttpClient import *

if __name__ == '__main__':
    httpClient = HttpClient()
    headers = [
        ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
        ('User-Agent',
         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
    ]
    # set headers
    httpClient.setHeaders(headers)
    
    url = "http://localhost:8080/auth/api/checkLogin"
    data = "token=-92mtvqrRJo@239"
    
    # GET
    url_data = url + "?" + data
    
    request = httpClient.doGet(url_data)
    print request  # {"rest":20525534516,"stat":"OK"}
    
    # POST
    data = {}
    data['token'] = '-92mtvqrRJo@239'
    
    # data to json
    httpClient.post_dataToJsonDump(data)
    request = httpClient.doPost(url, data)
    print request