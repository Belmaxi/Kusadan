from nonebot import on_command,on_message
from nonebot.typing import T_State
from nonebot.adapters import Event,Bot
import json
import time
import os
import random
backpack_status = on_command('背包')

@backpack_status.handle()
async def backpack_status_handle(bot:Bot,event:Event,state:T_State):
    st=''
    reply=[]
    qqnum = str(event.get_user_id())
    file = open('data//packdata//data.json', 'r', encoding='gbk')
    data = json.load(file)
    if qqnum in data:
        if len(data[qqnum])>0 and len(data[qqnum])<10:
            for i in data[qqnum].items():
                st += i[0]
                st += '*' + str(i[1])
                st += '\n'
            st=st[0:-1]
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
                        'text':'的背包：\n' + st
                    }
                }
            ]
            if event.get_event_name()[:15]=='message.private':
                reply[0]['type']='text'
                reply[0]['data'].pop('qq')
                reply[0]['data']['text']='你'
                
            await backpack_status.send(reply)
