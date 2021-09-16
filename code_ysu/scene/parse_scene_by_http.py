#!/usr/bin env python
# coding=utf-8

import json
import traceback
from urllib import request
from urllib import parse

has_res_count = 0
all_count = 0
spliter = '@@@'

def parse_json_in_str(data):
    # parse json and convert everything from unicode to st

    return json.loads(data)


def classify_queries(query_array):
    classify_result = []
    for query in query_array:
        try:
            encoded_query = urllib.quote(query.encode('utf8'))
        except BaseException:
            print('query %s exception' % (query))
        # seller_id = title2seller[1]
        url_template = 'xxx/intention.htm?q=%s' % (encoded_query)
        request_result = {}
        try:
            request_result = classify_query(url_template)
            classify_result.append(request_result)
        except BaseException:
            print('url_template has a problem:' + url_template)
            traceback.print_exc()
    return classify_result


def classify_query(url):
    # print(url)
    global all_count
    all_count += 1
    fd = request.urlopen(url)

    json_obj = {}
    data = fd.read()
    # print(data)
    if data != 'null':
        json_obj = parse_json_in_str(data)

    request_result = {}
    if json_obj:
        request_result = {'question': str(json_obj.get('question')), 'scene': str(json_obj.get('sceneKey')),
                          'packName': str(json_obj.get('packName'))}

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
        title = parse.quote(query2scene_key[0].encode('utf8'))
        # seller_id = title2seller[1]
        url_template = 'https://xxxx/intention.htm?q=%s' % (title)
        # try:
        #     startRequst(url_template)
        # except BaseException:
        #     print('url_template has a problem:' + url_template)
        #     traceback.print_exc()

    output_file.write('test res:' + str(has_res_count) + '/' + str(all_count))
    print('test res:' + str(has_res_count) + '/' + str(all_count))
