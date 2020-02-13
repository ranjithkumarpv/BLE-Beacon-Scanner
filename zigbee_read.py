#!/usr/bin/python
import serial
import time
import datetime
import glob
import MySQLdb
from xbee import ZigBee

serial_port = serial.Serial('/dev/ttyUSB0', 9600)

zb = ZigBee(serial_port)
 
# Variables for MySQL
db = MySQLdb.connect(host="localhost", user="root",passwd="root1", db="temp_database")
cur = db.cursor()

#print r.temperature


while True:
    try:
        datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
        data = zb.wait_read_frame() #Get data for later use
        #print data # for debugging only   
	value = str(zb.wait_read_frame()['samples'])
	str_a=value[11:14]
	b=10
	c= int(str_a) + b
	print c
	cur.execute ("""insert into tempLog Values(%s,%s)""",(datetimeWrite,c))
        db.commit()
    except KeyboardInterrupt:
        sel
        break
serial_port.close()
//cur.execute ("""insert into tempLog Values(%s,%s,%s,%s,%s,%s)""",(datetimeWrite,sp[0],sp[1],sp[2],sp[3],sp[4],sp[5]))
---------------

cur.execute ("""insert into tempLog Values(%s,%s,%s,%s,%s,%s)""",(datetimeWrite,MACADD,UDID,MAJOR,MINOR,TXPOWER,RSSI))
        db.commit();
        print "Write Complete"
