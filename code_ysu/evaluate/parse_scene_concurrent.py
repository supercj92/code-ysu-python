import json
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from parse_scene_by_http import classify_query
from urllib import parse, request
import excel_load
import sys


def parse_scene_in_multi_thread_mode(queries):
    count = 0
    futures = []
    with ThreadPoolExecutor(20) as executor:
        for query in queries:
            try:
                count += 1
                url_template = 'https://alibee-shop.taobao.org/alibee/intention.htm?q=%s' % parse.quote(
                    str(query).encode('utf8'))
                future = executor.submit(classify_query, url_template)
                futures.append(future)
            except BaseException:
                print('query %s exception' % (query))
                traceback.print_exc()
            if count % 100 == 0:
                print('count %d' % count)
    return futures

def parse_json_in_str(data):
    # parse json and convert everything from unicode to str
    return json.loads(data)

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


#  python3 /Users/chris/PycharmProjects/code-ysu-python/code_ysu/evaluate/parse_scene_concurrent.py
# /Users/chris/PycharmProjects/code-ysu-python/code_ysu/data/guangyun_test_query.xlsx ~/guangyun_res.csv
if __name__ == "__main__":
    start_time = time.time()
    corpus_path = sys.argv[1]
    output_file = sys.argv[2]
    print('start evaluating %s' % str(start_time))
    queries = excel_load.load_data_from_excel(corpus_path)
    futures = parse_scene_in_multi_thread_mode(queries[1:3])

    print('task submitted, start execute task')
    scene_results = []
    error_count = 0
    for future in futures:
        try:
            scene_results.append(future.result())
        except BaseException:
            error_count += 1

    print('task executed, start to write file')
    with open(output_file, 'a+') as output_file:
        for result in scene_results:
            output_file.write('%s,%s,%s\n' % (result.get('question'), result.get('scene'), result.get('packName')))

    end_time = time.time()
    print('finished, evaluating cost %d, error count %d' % (end_time - start_time, error_count))
