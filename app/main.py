#!/usr/bin/env python3

from flask import Flask, render_template, request
import sqlite3
from DB.initDB import createDB, insertData, extractData, getDBLine, modifyData, deleteData, getGliders
from datetime import date

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return(loadIndex())

@app.route('/supprLine', methods=["POST"])
def supprLine():
    result = dict(request.form)
    deleteData(result["id"])
    return(loadIndex())

@app.route('/newLine', methods=['POST'])
def newLine():
    result = dict(request.form)
    data = Data()
    data.loadGliders()
    if result["action"] == "new":
        data.lineData = ("", "", "", "", "", "", "", "")
        data.info = "new"
    elif result["action"] == "mod":
        data.lineData = getDBLine(result["id"])
        data.info = "mod"
        data.id = result["id"]
    return(render_template("newLine.html", data = data))

@app.route('/saveLine', methods=["POST"])
def saveLine():
    result = dict(request.form)
    if result["action"] == "new":
        insertData(result)
    elif result["action"] == "mod":
        modifyData(result["id"], result)
    return(loadIndex())

@app.route('/test')
def test():
    return(render_template("test.html"))

@app.route('/modLine', methods=["POST"])
def modLine():
    result = dict(request.form)
    data = getDBLine(result['id'])
    return(render_template("modLine.html", data = data))

class Data:
    def __init__(self):
        pass
    def loadDate(self):
        td = date.today()
        self.day = self.addZero(td.day, 2)
        self.month = self.addZero(td.month, 2)
        self.year = self.addZero(td.year, 4)
    def addZero(self, char, l):
        return(("0" + str(char))[-l:])
    def loadSQL(self):
        self.sqlData = list(sorted(extractData(), reverse = True, key = lambda x: timeToInt(x[5])))
    def loadGliders(self):
        self.gliders = dict(getGliders())

def timeToInt(value):
    return(int(value[:2]) * 60 + int(value[3:]))

def loadIndex():
    data = Data()
    data.loadDate()
    data.loadSQL()
    return(render_template("index.html", data = data))


if __name__ == "__main__":

    createDB()

    app.run(debug = True)
