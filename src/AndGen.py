# coding: utf-8

columes = []
db_columes = []

def readColumes():
    jfile = open("../resources/po/OrderFinanceFlowReq.java",  mode='r', encoding='UTF-8')
    lines = jfile.readlines()
    for line in lines:
        if line.__contains__('serialVersionUID'):
            continue
        if line.find("private") != -1:
            strs = line.split(" ")
            colume = strs[len(strs) - 1]\
                .replace(";", "")\
                .replace("\r", "")\
                .replace("\n", "")
            columes.append(colume)

def sqlFormat():
    for colume in columes:
        rc = ''
        for c in colume:
            if str.isupper(c):
                rc = rc + '_' + str.lower(c)
            else:
                rc = rc + c
        db_columes.append(rc)

def xmlGen():
    for i in range(len(columes)):
        tag = '<if test="%s != null">\n AND %s = #{%s}\n</if>' % (columes[i], db_columes[i], columes[i])
        print(tag)

if __name__ == '__main__':
    readColumes()
    sqlFormat()
    xmlGen()
