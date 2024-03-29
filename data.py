import sqlite3
import ct

def addlog(ip:str, bandwidth:int):
    """
    Insert data into database table(Bandwidth) with 'ip' and 'measured_bandwidth'.
    Return True/False.
    """
    
    # Check if bandwidth is an integer
    try:
        int(bandwidth)
    except ValueError:
        print("Error: bandwidth must be an integer.")
        print("Your input is:", bandwidth)
        return False
    
    # connect DB
    dbcon = ct.connect_db()  
    cursor = dbcon.cursor()  

    # insert data
    try:
        cursor.execute("INSERT INTO Bandwidth (ipv4_addr, measured_bandwidth) VALUES(?, ?)", (ip, bandwidth))
        dbcon.commit()
        return True
    except Exception as e:
        print("An error occured:", e)
        return False
    finally:
        dbcon.close()

def failcount(day:str, ip:str):
    """
    Search the result(array[24]) from database table(Device) with 'day' and 'ip'.
    Return array[24].
    """

    # formate of day is wrong，it should be like "2024-01-01"
    day = checkdateformat(day)

    # connect DB
    dbcon = ct.connect_db()  
    cursor = dbcon.cursor()  
    
    # collect 'measured_bandwidth' which square with 'ip' and 'day' from table(Bandwidth)
    cursor.execute("SELECT hms,measured_bandwidth FROM Bandwidth WHERE day = ? AND ipv4_addr = ?;", (day, ip,))
    
    
    # store in list(bandwidth)
    bandwidth = [[] for i in range(24)]
    for row in cursor.fetchall():
        hours = int(row[0].split(":")[0]) # ex, '05:55:55' -> 5
        bandwidth[hours].append(row[1])

    # find 'contract_bandwidth' which square with 'ip' from table(Device) 
    cursor.execute("SELECT contract_bandwidth FROM Device WHERE ipv4_addr = ?;", (ip,))
    contract_bandwidth = cursor.fetchone()
    
    #  calculating fail and missing traffic
    count = [] 
    for row in bandwidth:
        fail = 0
        miss = 12 - len(row)
        for m in row:
            #print(contract_bandwidth[0], type(contract_bandwidth[0]))
            if m < contract_bandwidth[0]:
                fail += 1
        count.append((fail, miss))
              
    # close
    dbcon.commit() 
    dbcon.close()  
   
    return count

def checkdateformat(day:str):
    """
    Check if 'day' is correct.
    If the format of day is '2024:01:01' or '2024:1:1' or '2024-1-1' or '2024/1/1' or '2024/01/01',
    this funciton would change the format into '2024-01-01'.
    If not the above format, it would print error.
    """
    from datetime import datetime
    
    # 2024:01:01 、2024-1-1 、2024/1/1
    formats = ["%Y:%m:%d", "%Y-%m-%d", "%Y/%m/%d"]
    for fmt in formats:
        try:
            return datetime.strptime(day, fmt).strftime("%Y-%m-%d")
        except ValueError:
            pass
    raise ValueError(f"Uknown format: {day}") # stop search

def listdevices():
    """
    Return all 'device_name' & 'ipv4_addr' in database
    """
    # connect DB
    dbcon = ct.connect_db() 
    cursor = dbcon.cursor() 

    listdevc = []

    # execute SQL
    cursor.execute("SELECT device_name, ipv4_addr FROM Device;")
    
    # return { 'device_name':'xxx', 'ipv4_addr':'xxx'}
    devices = cursor.fetchall()
    for row in devices:
        listdevc.append({'device_name': row[0], 'ipv4_addr':row[1]})
    

    # close
    dbcon.commit()
    dbcon.close()  

    return listdevc
