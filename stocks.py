#!/usr/bin/python3
# -*- coding: utf-8 -*-


import xml.dom.minidom

import sys
import os
import re

import mysql.connector



document = xml.dom.minidom.parse(sys.argv[1])
tableElements = document.getElementsByTagName('table')[2]

for tr in tableElements.getElementsByTagName('tr'):
    data = []

    for a in tr.getElementsByTagName('a'):
        for node in a.childNodes:
            if node.nodeType == node.TEXT_NODE:
                data.append(node.nodeValue)


    for td in tr.getElementsByTagName('td'):
        for node in td.childNodes:
            if node.nodeType == node.TEXT_NODE:
                data.append(node.nodeValue)

    del data[-1]
    del data[1]
    del data[1]
    del data[1]

    symbol = data[0]
    symm = re.findall(r"\(([A-Za-z0-9_]+)\)", symbol)

    sym = (''.join(symm))


    company = data[0]
    comp = re.sub("\(.*\)\n","", company)

    volume = data[1]
    lst = volume.replace(',', '')


    price = data[2]
    lstt = price.lstrip('$')


    chge = data[-1]

    con = mysql.connector.connect(host='localhost', user='root', password='root', database='tester')
    cur = con.cursor()
    cur.execute("INSERT INTO Info(exchge,symbol,company,volume,price,chge) VALUES (%s,%s,%s,%s,%s,%s)",("NYSE",sym,comp,lst,lstt,chge))
    cur.execute("UPDATE Info SET volume=%s,price=%s,chge=%s WHERE exchge='NYSE' AND symbol=%s",(volume,price,chge,sym))
    cur.execute("DELETE FROM Info WHERE volume='Price' and price='Chg'")
    con.commit()
    cur.close()
    con.close()

