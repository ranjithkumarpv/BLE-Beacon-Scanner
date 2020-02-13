# test BLE Scanning software
# jcs 6/8/2014
import time
import datetime
import glob
import MySQLdb
import blescan
import sys

import bluetooth._bluetooth as bluez

# Variables for MySQL
db = MySQLdb.connect(host="localhost", user="root",passwd="pvr", db="Ble_database")
cur = db.cursor()

dev_id = 0
try:
        datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"
	
except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)


while True:
	returnedList = blescan.parse_events(sock, 10)
	print "----------"
	for beacon in returnedList:
		sp=beacon.split(',');
		MACADD=sp[0];
		UDID=sp[1];
		MAJOR=sp[2];
		MINOR=sp[3];
		TXPOWER=sp[4];
		RSSI=sp[5];
		print sp[0];
		print sp[1];
		print sp[2];
		print sp[3];
		print sp[4];
		print sp[5];
		
		cur.execute ("""insert into BleLog Values(%s,%s,%s,%s,%s,%s,%s)""",(datetimeWrite,MACADD,0,MAJOR,MINOR,TXPOWER,RSSI))
                db.commit();
                print "Write Complete"
		
        
       
