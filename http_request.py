#!/usr/bin env python

import urllib2
import json
import urllib

has_res_count = 0
all_count = 0

def startRequst(url):
    print url
    global all_count
    all_count += 1
    req = urllib2.Request(url)
    #req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36')

    fd = urllib2.urlopen(req)

    output_path = './output.data'
    output_file = open(output_path, 'a+')

    jsonObj = {}
    data = fd.read()
    #print data
    if(data != 'null'):
        jsonObj = parse_json_in_str(data)

    if jsonObj:
        output_file.write(str(jsonObj.get('itemId')))
        output_file.write('\n')
        global has_res_count
        has_res_count += 1
    else:
        output_file.writelines(data + '\n')

def parse_json_in_str(data):
    # parse json and convert everything from unicode to str
    return json.loads(data)

if __name__ == "__main__":
    config_path = './input.data'
    config = {}
    arr = []
    with open(config_path, 'rb') as f:
        while True:
            line = f.readline().decode('utf8')
            if line:
                arr.append(line)
            else:
                break
    for item in arr:
        title2seller = item.split(',')
        title = urllib.quote(title2seller[0].encode('utf8'))
        seller_id = title2seller[1]
        url_template = 'http://www.taobao.com?title=%s&sellerId=%s'%(title, seller_id)
        startRequst(url_template)

    print 'test res:' +  str(has_res_count) + '/' +  str(all_count)