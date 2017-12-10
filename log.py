# -*- coding: utf-8 -*-
import time


def logging(message):
    file = open('bot.log', 'a')
    currentTime = time.ctime(time.time())
    var = ("| %.24s | %-12i | %s %s | %s | %s \n" % (currentTime, message.from_user.id, message.from_user.first_name, message.from_user.last_name, str(message.from_user.id), message.text))
    file.write(var)
    file.close()
