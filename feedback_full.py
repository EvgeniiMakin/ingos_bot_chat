# -*- coding: utf-8 -*-
import time


def log_feedback_full(message, answer):
    file = open('bot_feedback_full.log', 'a')
    currentTime = time.ctime(time.time())
    var = ("| %.24s | %-12i | %s %s | %s | %s \n" % (currentTime, message.from_user.id, message.from_user.first_name, message.from_user.last_name, str(message.from_user.id), answer))
    file.write(var)
    file.close()
