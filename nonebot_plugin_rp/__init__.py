import time
import os
import random
import hashlib
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

__plugin_name__ = '今日人品'
__plugin_usage__ = "发送rp或者今日人品来获取今天的人品"


def Hash(s: str):
    h = 1
    num = 1
    for i in s:
        h = h+33 * ord(i) * num
        num += 1
    return h


rp=on_command(('rp'))
@rp.handle()
async def rp_(bot:Bot,event:Event,state:T_State):
    qqnum = str(event.get_user_id())
    dayline = time.ctime()
    dayline = dayline.split()
    del dayline[3]
    del dayline[0]
    dayline = ''.join(dayline)
    dayline += qqnum
    dayline = Hash(dayline)
    dayline = dayline % 100 + 1

    rely=[
        {
            'type':'at',
            'data':{
                'qq':qqnum
            }
        },
        {
            'type':'text',
            'data':{
                'text':"今天的人品是："+str(dayline)
            }
        }
    ]
    if event.get_event_name()[:15]=='message.private':
        rely[0]['type']='text'
        rely[0]['data'].pop('qq')
        rely[0]['data']['text']='你'
    await rp.send(rely)