def parse():
    while 1:
        input = raw_input()
        array = input.split('@')
        print_array(array)


def print_array(array):
    print 'userId:' + array[0]
    print 'traceId:' + array[1]
    print 'classifySceneKey:' + array[2]


if __name__ == "__main__":
    print 'please input str:'
    parse()
