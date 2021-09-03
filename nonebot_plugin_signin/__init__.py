from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Event,Bot
import json
import time
import os
import random

sign_in=on_command('签到')
@sign_in.handle()
async def sign_in_handle(bot:Bot,event:Event,state:T_State):
    qqnum = str(event.get_user_id())
    reply=[]
    r = random.randint(30, 150)
    file=open('data\\signindata\\data.json','r',encoding='utf-8')
    data=json.load(file)
    dayline = time.ctime()
    dayline = dayline.split()
    del dayline[3]
    del dayline[0]
    dayline = ''.join(dayline)
    if qqnum in data:
        if data[qqnum]['lastday'] == dayline:
            await sign_in.send('你今天签到过了哦，不要重复签到')
        else:
            lable=0
            if data[qqnum]['continuity'] - round(time.time() + 28800) // 86400 == -1: #上一次和这一次的签到时间差差1天
                data[qqnum]['continuity'] += 1
                data[qqnum]['连续签到'] += 1
            elif data[qqnum]['continuity'] - round(time.time() + 28800) // 86400 != 0:
                data[qqnum]['continuity'] = round(time.time() + 28800) // 86400
                data[qqnum]['连续签到'] = 1
                lable=1

            data[qqnum]['累计签到'] += 1
            data[qqnum]['星星'] += r
            reply = [
                {
                    'type':'at',
                    "data":{
                        'qq':qqnum
                    }
                },
                {
                    'type':'text',
                    "data":{
                        'text':'\n' + '身份：' + str(data[qqnum]['身份']) + '\n累计签到：' + str(data[qqnum]['累计签到']) + '天\n连续签到：' + str(data[qqnum]['连续签到']) + '天\n今天获得的星星：' + str(r) +  '颗\n累计星星数量：' + str(data[qqnum]['星星']) + '颗\n今天的你，也要元气满满哦~'
                    }
                }
            ]
            if data[qqnum]['lastday'] == dayline:
                await sign_in.send('你今天签到过了哦')
            else:
                await sign_in.send(reply)
                if lable==1:
                    await sign_in.send('你今天断签了哦，可惜了')

            data[qqnum]['lastday'] = dayline
            with open('data\\signindata\\data.json', 'w' ,encoding='utf-8') as f:
                json.dump(data, f, indent=4)
    else:
        f=open('data\\signindata\\data.json','w',encoding='utf-8')
        data[qqnum]={}
        data[qqnum]['身份'] = '普通人'
        data[qqnum]['累计签到'] = 1
        data[qqnum]['连续签到'] = 1
        data[qqnum]['星星'] = r
        data[qqnum]['lastday'] = dayline
        data[qqnum]['continuity'] = round(time.time()) // 86400
        reply = [
            {
                'type': 'at',
                "data": {
                    'qq': qqnum
                }
            },
            {
                'type': 'text',
                "data": {
                    'text': '\n' + '身份：' + str(data[qqnum]['身份']) + '\n累计签到：' + str(
                        data[qqnum]['累计签到']) + '天\n连续签到：' + str(data[qqnum]['连续签到']) + '天\n今天获得的星星：' + str(
                        r) + '颗\n累计星星数量：' + str(data[qqnum]['星星']) + '颗\n今天的你，也要元气满满哦~'
                }
            }
        ]
        json.dump(data,f,indent=4)
        await sign_in.send(reply)

Search=on_command('查询状态')
@Search.handle()
async def Search_handle(bot:Bot,event:Event,state:T_State):
    qqnum = str(event.get_user_id())
    file = open('data\\signindata\\data.json', 'r', encoding='utf-8')
    data = json.load(file)
    reply = [
        {
            'type': 'at',
            "data": {
                'qq': qqnum
            }
        },
        {
            'type': 'text',
            "data": {
                'text':'是一名' + data[qqnum]['身份'] + '\n一共签到了竟然有' + str(data[qqnum]['累计签到']) + '天\n连续签到' + str(data[qqnum]['连续签到']) + '天\n总计有' + str(data[qqnum]['星星']) + '颗星星'

            }
        }
    ]
    if qqnum in data:
        await Search.send(reply)
    else:
        await Search.send('你是一个普通人')
