#!/usr/bin env python

import urllib2
import json
import urllib
import sys
import traceback
import threadpool
import time
reload(sys)
sys.setdefaultencoding('utf-8')

has_res_count = 0
all_count = 0
output_path = './output_multi.data'
output_file = open(output_path, 'a+')
error_url = './error_url.data'
error_url_file = open(error_url, 'a+')
spliter = '@@@'
error_url_array = []

def startRequst(url):
    print url
    global all_count
    all_count += 1
    req = urllib2.Request(url)
    #req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36')

    fd = urllib2.urlopen(req)

    jsonObj = {}
    data = fd.read()
    #print data
    if(data != 'null'):
        jsonObj = parse_json_in_str(data)

    if jsonObj:
        res_str = ''
        res_str += str(jsonObj.get('question'))
        res_str += spliter
        sceneKey = str(jsonObj.get('sceneKey'))
        res_str += sceneKey
        res_str += spliter
        sceneKeyEqual = ('sk_tuihuoyunfei' == sceneKey)
        res_str += str(sceneKeyEqual)
        output_file.write(res_str + '\n')
        global has_res_count
        if sceneKeyEqual:
            has_res_count += 1
    else:
        output_file.writelines(data + '\n')

def parse_json_in_str(data):
    # parse json and convert everything from unicode to str
    return json.loads(data)

def startRequstHandledException(url_template):
    try:
        startRequst(url_template)
    except BaseException:
        global all_count
        all_count -= 1
        print 'url_template has a problem:' + url_template
        error_url_array.append(url_template)
        traceback.print_exc()

if __name__ == "__main__":
    config_path = './input_multi.data'
    config = {}
    data_array = []
    star_time = time.time()
    with open(config_path, 'rb') as f:
        while True:
            line = f.readline().decode('utf8')
            if line:
                data_array.append(line)
            else:
                break

    url_arr = []
    for item in data_array:
        query2scene_key = item.split('sk_tuihuoyunfei')
        query = urllib.quote(query2scene_key[0].encode('utf8'))
        #seller_id = title2seller[1]
        url_template = 'https://xxx/intention.htm?q=%s'%(query)
        url_arr.append(url_template)

    pool = threadpool.ThreadPool(8 + 2)
    requests = threadpool.makeRequests(startRequstHandledException, url_arr)
    [pool.putRequest(req) for req in requests]
    pool.wait()
    print '%d second'%(time.time() -star_time)
    print 'error url array start'

    #记录异常的请求
    error_url_str = ''
    for error_url in error_url_array:
        error_url_str = error_url_str + '\n' + error_url
        #startRequstHandledException(error_url)
    error_url_file.write(error_url_str)
    error_url_file.close()

    output_file.write('test res:' +  str(has_res_count) + '/' +  str(all_count))
    output_file.close()
    print 'test res:' +  str(has_res_count) + '/' +  str(all_count)