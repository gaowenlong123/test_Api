def write_text_init(path='b.txt'):
    data = '接口统计   只存一次运行\n'
    with open(path, 'w+') as f:
        f.write(data)

def write_text_add(data,path='b.txt'):

    with open(path, 'w') as f:
        f.write(data)

def write_text(data, path):
    #累加
    all = read_text(path)
    data+='\n'
    all+=data
    with open(path, 'w+') as f:
        f.write(all)

def read_text(path ):
    #读数据
    with open(path, 'r+') as f:
        data=f.read()
    f.close()
    return data

def read_text_by_gbk(path ):
    #读数据
    with open(path, mode='rb') as f:
        data=f.read()
    f.close()
    return data





if __name__ == '__main__':
    # a=read_text('b.text')
    from Api_Server.Support.Base_Enums import *


    # write_text('aaccccccccccc','b.text')