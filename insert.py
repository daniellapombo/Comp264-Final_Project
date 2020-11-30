#!/usr/bin/python3

from datetime import date, datetime
import mysql.connector
import subprocess
import re

dbc = mysql.connector.connect(host="127.0.0.1", user="root", password="1234", database="Temperature")

cursor = dbc.cursor()

today = date.today()
now = datetime.now()

#taking output of bash script and turning it into usable int to add to database
#bash = subprocess.Popen(['./printTemp.sh'], stdout=subprocess.PIPE)
bash = subprocess.check_output('./printTemp.sh')

bash = str(bash)
bashList = bash.split("'")

bash = bashList[1]
bashList = bash.split("\\")
bash = bashList[0]
bash = float(bash)

addEntry = ("INSERT INTO Temperature (Degrees, Date) VALUES (%(bash)s, now())")

variables = {
	'bash': bash,
	'today': today,
	'now': now,
}

cursor.execute(addEntry, variables)

dbc.commit()
cursor.close()
dbc.close()
