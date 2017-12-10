# -*- coding: utf-8 -*-

import sqlite3
import hashlib
import config

def createNewUserAdmin(tg_id, password, role):
    db = sqlite3.connect(config.db_name)
    cursor = db.cursor()
    password = hashlib.sha256(bytes(password, encoding="UTF-8")).hexdigest()
    cursor.execute("INSERT INTO users (tg_id,password,role) VALUES (?,?,?)", (tg_id, password, role))
    db.commit()
    cursor.close()
    db.close()
    return True

def createNewUser(message):
    tg_id = message.from_user.id
    password = message.text[10:]
    role = "user"
    db = sqlite3.connect(config.db_name)
    cursor = db.cursor()
    password = hashlib.sha256(bytes(password, encoding="UTF-8")).hexdigest()
    cursor.execute("INSERT INTO users (tg_id,password,role) VALUES (?,?,?)", (tg_id, password, role))
    db.commit()
    cursor.close()
    db.close()
    return True


def isUserInDB(message):
    tg_id = message.from_user.id
    db = sqlite3.connect(config.db_name)
    cursor = db.cursor()
    cursor.execute(("SELECT id FROM users WHERE tg_id = '%s'" % str(tg_id)))
    var = cursor.fetchone()
    if var is not None:
        return True
    else:
        return False
    db.commit()
    cursor.close()
    db.close()


def authorization(message):
    tg_id = message.from_user.id
    password = message.text[10:]
    db = sqlite3.connect(config.db_name)
    cursor = db.cursor()
    password = hashlib.sha256(bytes(password, encoding="UTF-8")).hexdigest()
    cursor.execute(("SELECT password FROM users WHERE tg_id = '%s'" % str(tg_id)))
    db_password = cursor.fetchone()
    cursor.close()
    if password == db_password[0]:
        login(tg_id)
        if isUserLoggedIn(message):
            return True
        else:
            return False
    else:
        return False
    db.commit()
    cursor.close()
    db.close()


def login(tg_id):
    db = sqlite3.connect(config.db_name)
    cursor = db.cursor()
    cursor.execute("UPDATE users SET isLogged = 1 WHERE tg_id = %s;" % tg_id)
    db.commit()
    cursor.close()
    db.close()


def isUserLoggedIn(message):
    tg_id = message.from_user.id
    db = sqlite3.connect(config.db_name)
    cursor = db.cursor()
    cursor.execute(("SELECT isLogged FROM users WHERE tg_id = '%s'" % str(tg_id)))
    var = cursor.fetchone()
    if var[0] == 1:
        return True
    else:
        return False
    db.commit()
    cursor.close()
    db.close()


def logoutAll():
    db = sqlite3.connect(config.db_name)
    cursor = db.cursor()
    cursor.execute("UPDATE users SET isLogged = 0")
    db.commit()
    cursor.close()
    db.close()


def logoutUser(message):
    tg_id = message.from_user.id
    db = sqlite3.connect(config.db_name)
    cursor = db.cursor()
    cursor.execute("UPDATE users SET isLogged = 0 WHERE tg_id = %s;" % tg_id)
    db.commit()
    cursor.close()
    db.close()
if __name__ == '__main__':
    createNewUserAdmin(config.telegramID, config.PASSWORD, 'admin')