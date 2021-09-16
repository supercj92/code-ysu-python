def parse():
    while True:
        input_str = input("place input:")
        array = input_str.split('@')
        print_array(array)


def print_array(array):
    print('userId:' + array[0])
    print('traceId:' + array[1])
    print('classifySceneKey:' + array[2])


if __name__ == "__main__":
    parse()
