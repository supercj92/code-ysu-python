
def parse():
    while 1:
        input = raw_input()
        array = input.split('@')
        printArray(array)

def printArray(array):
    print 'userId:' + array[0]
    print 'traceId:' + array[3]
    print 'classifySceneKey:' + array[16]

if __name__ == "__main__":
    print 'please input str:'
    parse()