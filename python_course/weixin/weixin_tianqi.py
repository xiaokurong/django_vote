# coding: utf-8
from __future__ import unicode_literals
from wxpy import *
from wechat_sender import listen
bot = Bot('bot.pkl')
receivers=[]
receivers.append(bot.file_helper)
print(receivers)
listen(bot,receivers=receivers)
