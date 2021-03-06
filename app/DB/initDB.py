#!/usr/bin/env python3

import sqlite3
from datetime import date

def getStrDay():
    td = date.today()
    def addZero(char, l):
        return(("0" + str(char))[-l:])
    return("DB" + addZero(td.day, 2) + addZero(td.month, 2) + addZero(td.year, 4))

def getGliders():
    conn = sqlite3.connect("DB/gliders.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM glider")
    return(cursor.fetchall())

def createDB():
    conn = sqlite3.connect("DB/base.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS " + getStrDay() + """(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    cn TEXT,
    immat TEXT,
    pilot TEXT,
    copilot TEXT,
    takeofftime TEXT,
    landingtime TEXT,
    plane TEXT,
    addinfo TEXT
    )""")
    conn.commit()
    conn.close()

def modifyData(id, data):
    conn = sqlite3.connect("DB/base.db")
    cursor = conn.cursor()
    sql = "UPDATE " + getStrDay() + " SET "
    for key in ("cn", "immat", "pilot", "copilot", "takeofftime", "landingtime", "plane", "addinfo"):
        sql += key + " = '" + data[key].replace("'", " ") + "', "
    sql = sql[:-2] + " WHERE id = '" + id + "'"
    cursor.execute(sql)
    conn.commit()
    conn.close()

def insertData(data):
    conn = sqlite3.connect("DB/base.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO " + getStrDay() + """(
    cn, immat, pilot, copilot, takeofftime, landingtime, plane, addinfo)
    VALUES(:cn, :immat, :pilot, :copilot, :takeofftime, :landingtime, :plane, :addinfo)
    """, data)
    conn.commit()
    conn.close()

def deleteData(id):
    conn = sqlite3.connect("DB/base.db")
    cursor = conn.cursor()
    sql = "DELETE from " + getStrDay() + " WHERE id = " + str(id)
    cursor.execute(sql)
    conn.commit()
    conn.close()

def extractData():
    conn = sqlite3.connect("DB/base.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM " + getStrDay())
    return(cursor.fetchall())

def getDBLine(id):
    conn = sqlite3.connect("DB/base.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM " + getStrDay() + " WHERE id = " + str(id))
    return(cursor.fetchone())
