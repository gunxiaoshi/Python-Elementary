#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Jianfeng Ding  Time: 2018/7/23

data = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村': {
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地': {
                '百度':{},
            }
        },
        "昌平": {
            "沙河": ["oldboy", "test"],
            "天通苑": ["链家地产", "我爱我家"],
            "回龙观": {},
        },
        "朝阳": {
            "望京": ["奔驰", "陌陌"],
            "国贸": ["CICC", "HP"],
            "东直门": ["Advent", "飞信"],
        },
        '东城': {},
    },
    '上海': {
        '闵行': {
            '人民广场': ['炸鸡店'],
            },
        '闸北': {
            '火车战': ['携程'],
        },
        '浦东': {},
    },
}

while True:
    for i in data:
        print(i)

    choice = input("选择进入1>>>:")
    if choice in data:
        while True:
            for i2 in data[choice]:
                print("\t", i2)
            choice2 = input("选择进入2>>>:")

            if choice2 in data[choice]:
                while True:
                    for i3 in data[choice][choice2]:
                        print("\t\t", i3)
                    choice3 = input("选择进入3>>>:")

                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print("\t\t\t",i4)
                        choice4 = input("最后一层，按b返回>>>:")

                        if choice4 == "b":
                            pass
                    if choice3 == "b":
                        break
            if choice2 == "b":
                break





