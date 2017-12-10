# -*- coding: utf-8 -*-
import sqlite3
import config

db = sqlite3.connect(config.db_name)
cursor = db.cursor()
cursor.execute('''CREATE TABLE `users` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `tg_id` TEXT NOT NULL UNIQUE,
    `password`  TEXT NOT NULL,
    `role`  TEXT NOT NULL DEFAULT 'user',
    `isLogged`  INTEGER NOT NULL DEFAULT 1
);''')
db.commit()
cursor.close()
db.close()
