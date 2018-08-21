# coding: utf-8

columes = []
db_columes = []
classPath = ''

def readColumes():
    jfile = open("../resources/po/VehicleDisabledRecord.java",  mode='r', encoding='UTF-8')
    lines = jfile.readlines()
    for line in lines:
        if line.find('serialVersionUID') != -1:
            continue
        if line.find('package') != -1:
            classPath = line[line.find('com'): len(line) - 2]
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
    print('<resultMap id="BaseResultMap" type="%s">' % classPath)
    for i in range(len(columes)):
        tag = '<result column="%s" property="%s" />' % (db_columes[i], columes[i])
        print(tag)
    print('</resultMap>')

if __name__ == '__main__':
    readColumes()
    sqlFormat()
    xmlGen()
