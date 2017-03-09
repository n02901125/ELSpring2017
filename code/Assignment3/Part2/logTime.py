#!/usr/bin/python
import os
import time
import sqlite3

def logTime():
        [cd, ct] = readTime()
        con=sqlite3.connect('testTime.db')
        c = con.cursor()
        c.execute("INSERT INTO time VALUES (?,?)", (cd, ct))
        con.commit()
        for row in c.execute('SELECT * FROM time'):
                print row
        con.close()
        status = "Log Successful"
        return status

def readTime():
        currentTime=time.strftime('%H-%M-%S')
        currentDate=time.strftime('%Y-%m-%d')
        return[currentDate, currentTime]

print logTime()
