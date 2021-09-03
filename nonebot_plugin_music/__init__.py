from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Event,Bot
import json
import time
import os
import random
import requests
header={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
music = on_command('点歌')
@music.handle()
async def music_handle(bot:Bot,event:Event,state:T_State):
    args = event.get_message().extract_plain_text()
    if args:
        url='http://shengapi.cn/api/wy.php?msg=' + args + '&n=1'
        re=requests.get(url=url,headers=header)
        text = re.text.split()
        q=[text[0].split('：')[-1] , text[1].split('：')[-1] , text[2].split('：')[-1] , text[3].split('：')[-1]]
        reply = [
            {
                "type": "music",
                "data": {
                    "type": "custom",
                    "url": q[3],
                    "image": q[0],
                    "title": q[1],
                    "content": q[2]
                }
            }
        ]
        await music.send(reply)

music163 = on_command('网易云点歌')
@music163.handle()
async def music163_handle(bot:Bot,event:Event,state:T_State):
    args = event.get_message().extract_plain_text()
    if args:
        url = 'http://shengapi.cn/api/wy.php?msg=' + args + '&n=1'
        re = requests.get(url=url, headers=header)
        text = re.text.split()
        q = text[-1].split('=')[-1]
        reply = [
            {
                "type": "music",
                "data": {
                    "type": "163",
                    "id": q
                }
            }
        ]
        await music.send(reply)
