import sqlite3
import sys
import subprocess
from solomon import myInput as input

def create_table():
    """
    1. insert .sql to create table.
    2. insert the test file of Bandwidth and Device with csv.
    """

    # connect DB
    dbcon = connect_db()
    cursor = dbcon.cursor()
    
    # 讓 FOREIGN KEYS 有作用
    cursor.execute("PRAGMA FOREIGN_KEYS = ON")

    # create TABLE use sqlite command
    subprocess.run(["sqlite3", database, ".read Bandwidth.sql"])
    subprocess.run(["sqlite3", database, ".read Device.sql"])

    # insert file use sqlite command -- for test
    bandwidth_csv = input("Enter csv file of bandwidth:[{}] ", 'Bandwidth.csv')
    if bandwidth_csv != "":
        code = ".import " +  bandwidth_csv + " Bandwidth"
        subprocess.run(["sqlite3", database, ".mode csv", code, ".exit"])

    device_csv = input("Enter csv file of device:[{}] ", 'Device.csv')
    if device_csv != "":
        code = ".import " + device_csv + " Device"
        subprocess.run(["sqlite3", database, ".mode csv", code, ".exit"])
    
    #close
    dbcon.commit()
    dbcon.close()
    
def connect_db():
    """
    Connect to database.
    """

    # enter database   
    global database

    if len(sys.argv) > 1 and sys.argv[1] != "":         
        database = sys.argv[1]             
    else:
        database = input("Please enter database name:[{}] ", 'NCPB.db')  
        #database = "NCPB2.db"
        dbcon = sqlite3.connect(database) 
    return dbcon
