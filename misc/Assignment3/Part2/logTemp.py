#!/usr/bin/python
import os
import time
import sqlite3

""" Log Current Time, Temperature in Celsius and Fahrenheit
        Returns a list [time, tempC, tempF] """

#runs readTemp(), the commits data to db
def logTemp():
        [ct, tc, tf] = readTemp()
        con=sqlite3.connect('testTemp.db')
        c = con.cursor()
        c.execute("INSERT INTO temp VALUES (?,?,?)", (ct, tc, tf))
        con.commit()
        con.close()
        status = "Log Successful"
        return status

def readTemp():
        tempfile = open("/sys/bus/w1/devices/28-0000069757fc/w1_slave")
        tempfile_text = tempfile.read()
        currentTime=time.strftime('%x %X %Z')
        tempfile.close()
        tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
        tempF=tempC*9.0/5.0+32.0
        return [currentTime, tempC, tempF]

#from 0 to 20, logs time and waits 30 sec to run again.
for x in range (0, 20):		
        print logTemp()
	time.sleep(30)
