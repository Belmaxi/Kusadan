from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Event,Bot
import json
import time
import os
import random

def update_setu():
    reply = [
        {
            "type": "image",
            'data': {
                'file': 'http://shengapi.cn/api/image/peacg.php?id=' + str(random.randint(0,233333333))
            }
        }
    ]
    return reply
setu = on_command('来份美图')
@setu.handle()
async def setu_handle(bot:Bot,event:Event,state:T_State):
    await setu.send(update_setu())