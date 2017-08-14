#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import json
import copy
import re

if __name__ == '__main__':
    file = open('lesson_2.txt','r')
    data = []
    while 1:
        line = file.readline().strip()
        if not line:
            break
        paras = line.split('\t')
        lesson = {}
        lesson['id'] = paras[0]
        lesson['name'] = paras[1]
        lesson['type'] = paras[2]
        lesson['score'] = paras[3]
        lesson['teacher'] = paras[4]
        if not lesson['teacher'].strip():
            continue
        try:
            lesson['info1'] = paras[9]
        except Exception,e:
            lesson['info1'] = ''
        try:
            lesson['info2'] = paras[10]
        except Exception,e:
            lesson['info2'] = ''
        for k in lesson:
            print k, lesson[k]
        print ""

