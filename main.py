#!/usr/bin/env python3

from flask import Flask, render_template, request
import sqlite3
from DB.initDB import createDB, insertData, extractData
from datetime import date

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    data = Data()
    return(render_template("index.html", data = data))

@app.route('/newLine', methods=['POST'])
def newLine():
    return(render_template("newLine.html"))

@app.route('/saveLine', methods=["POST"])
def saveLine():
    result = request.form
    insertData(result)
    data = Data()
    return(render_template("index.html", data = data))

class Data:
    def __init__(self):
        self.loadDate()
        self.loadSQL()
    def loadDate(self):
        td = date.today()
        self.day = self.addZero(td.day, 2)
        self.month = self.addZero(td.month, 2)
        self.year = self.addZero(td.year, 4)
    def addZero(self, char, l):
        return(("0" + str(char))[-l:])
    def loadSQL(self):
        self.sqlData = reversed(extractData())


if __name__ == "__main__":

    createDB()

    app.run(debug = True)
