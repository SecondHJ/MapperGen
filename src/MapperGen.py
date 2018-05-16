# coding: utf-8
import os

columes = []
db_columes = []
po_dir = '../resources/po'



def loadfiles():
    for parent, dirnames, filenames in os.walk(po_dir):
        for filename in filenames:
            readColumes(filename)


def readColumes(fileName):
    print(po_dir + '/' + fileName)
    jfile = file(po_dir + '/' + fileName)
    lines = jfile.readlines()
    for line in lines:
        if line.find("private") != -1:
            strs = line.split(" ")
            colume = strs[len(strs) - 1].replace(";", "").replace("\n", "")
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
        tag = '<if test="%s != null">\n    AND %s = #{%s}\n</if>' % (columes[i], db_columes[i], columes[i])
        print(tag)


if __name__ == '__main__':
    loadfiles()
    sqlFormat()
    xmlGen()
