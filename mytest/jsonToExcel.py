from collections import namedtuple
import time

import json






def json2excel(args):
    print(len(args))
    mylist=[]
    for i in range(0,len(args)):
        a = json.load(open(args[i], encoding='utf8'))
        # print(a)
        json_str = json.dumps(a)
        data = json.loads(json_str, object_hook=lambda d: namedtuple('data', d.keys())(*d.values()))
        print(data)
        # print(data.body.list)
        ownlist = data.body.list
        mylist+=ownlist
    print(len(mylist))
    # print("===================================")
    # for i in range(0, len(mylist)):
    #     line=0
    #     print(mylist[i].liveId)
    #     line+=1
    #     # time.strftime(mylist[i].startTime,"yyyy-MM-dd")
    #     print( mylist[i].startTime)
    #     line+=1
    #     print(mylist[i].endTime)
    #     line=0
    # print("===================================")


def writeLivingCountAndTime(json):
    json_str = json.dumps(json)
    data = json.loads(json_str, object_hook=lambda d: namedtuple('data', d.keys())(*d.values()))
    print(data)


if __name__ == '__main__':
    # jsfile = ['E:\pythonProject\images\jjamicci_1.json','E:\pythonProject\images\jjamicci_2.json']
    # json2excel(jsfile)
    # print(time.localtime())
    print(1,2,3)
