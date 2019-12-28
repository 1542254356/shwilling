from pickle_dump import load_from_file

def filter(filterItem, value):
    list = []
    dataList = load_from_file()
    for item in dataList:
        if item[filterItem] == value:
            list.append(item)
    return list

if __name__ == '__main__':
    list = filter('editor', '常海月')
    print(list)