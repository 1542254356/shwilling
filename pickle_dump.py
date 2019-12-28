import pickle
from shwilling import getAllDatas

fileName = 'dataList.dump'

def dump_to_file():
    data = getAllDatas()
    f = open(fileName, 'wb')
    pickle.dump(data, f)
    f.close()

def load_from_file():
    f = open(fileName, 'rb')
    date = pickle.load(f)
    f.close()
    return date

if __name__ == '__main__':
    # dump_to_file()
    data = load_from_file()
    print(data)