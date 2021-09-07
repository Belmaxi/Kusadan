from nonebot import on_command,on_message
from nonebot.typing import T_State
from nonebot.adapters import Event,Bot
import json
import time
import os
import random
#签到插件拓展插件--身份插件 identity
identity=on_message()
identity_list=['炼星人（SmeltStar）']
@identity.handle()
async def identity_handle(bot:Bot,event:Event,state:T_State):
    r = random.randint(0, 1000)
    if r==1:
        qqnum = str(event.get_user_id())
        reply=[]
        file=open('data//signindata//data.json','r',encoding='utf-8')
        data=json.load(file)
        if qqnum in data:
            if data[qqnum]['身份']=='普通人':
                ran=identity_list[0]
                #ran=identity_list[random.randint(0,len(identity_list))]
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
                            'text':'\n领悟了什么~成为了一名' + ran
                        }
                    }
                ]
                data[qqnum]['身份'] = ran
                await identity.send(reply)
                with open('data\\signindata\\data.json', 'w' ,encoding='utf-8') as f:
                    json.dump(data, f, indent=4)
