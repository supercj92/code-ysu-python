#!/usr/bin env python

import urllib2
import json
import urllib
import sys
import traceback

reload(sys)
sys.setdefaultencoding('utf-8')

has_res_count = 0
all_count = 0
output_path = './output.data'
output_file = open(output_path, 'a+')
spliter = '@@@'


def startRequst(url):
    print url
    global all_count
    all_count += 1
    req = urllib2.Request(url)
    # req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36')

    fd = urllib2.urlopen(req)

    jsonObj = {}
    data = fd.read()
    # print data
    if (data != 'null'):
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

def classify_queries(query_array):
    classify_result = []
    for query in query_array:
        try:
            encoded_query = urllib.quote(query.encode('utf8'))
        except BaseException:
            print 'query %s exception' % (query)
        # seller_id = title2seller[1]
        url_template = 'xxx/intention.htm?q=%s' % (encoded_query)
        request_result = {}
        try:
            request_result = classify_query(url_template)
            classify_result.append(request_result)
        except BaseException:
            print 'url_template has a problem:' + url_template
            traceback.print_exc()
    return classify_result


def classify_query(url):
    #print url
    global all_count
    all_count += 1
    req = urllib2.Request(url)
    fd = urllib2.urlopen(req)

    jsonObj = {}
    data = fd.read()
    # print data
    if (data != 'null'):
        jsonObj = parse_json_in_str(data)

    request_result = {}
    if jsonObj:
        request_result = {'question': str(jsonObj.get('question')), 'scene': str(jsonObj.get('sceneKey')),
                          'packName': str(jsonObj.get('packName'))}

    return request_result


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
        query2scene_key = item.split('sk_tuihuoyunfei')
        title = urllib.quote(query2scene_key[0].encode('utf8'))
        # seller_id = title2seller[1]
        url_template = 'https://xxxx/intention.htm?q=%s' % (title)
        try:
            startRequst(url_template)
        except BaseException:
            print 'url_template has a problem:' + url_template
            traceback.print_exc()

    output_file.write('test res:' + str(has_res_count) + '/' + str(all_count))
    print 'test res:' + str(has_res_count) + '/' + str(all_count)
