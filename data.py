import sqlite3
import ct

def addlog(ip:str, bandwidth:str):
    """
    Insert data into database table(Bandwidth) with 'ip' and 'measured_bandwidth'.
    Return True/False.
    """

    # connect DB
    dbcon = ct.connect_db()  
    cursor = dbcon.cursor()  

    # insert data
    try:
        cursor.execute("INSERT INTO Bandwidth (ipv4_addr, measured_bandwidth) VALUES(?, ?)", (ip, bandwidth))
        dbcon.commit()
        return 1
    except Exception as e:
        print("An error occured:", e)
        return 0
    finally:
        dbcon.close()

def failcount(day:str, ip:str):
    """
    Search the result(array[24]) from database table(Device) with 'day' and 'ip'.
    Return array[24].
    """

    # connect DB
    dbcon = ct.connect_db()  
    cursor = dbcon.cursor()  
    
    # collect 'measured_bandwidth' which square with 'ip' and 'day' from table(Bandwidth)
    cursor.execute("SELECT hms,measured_bandwidth FROM Bandwidth WHERE day = ? AND ipv4_addr = ?;", (day, ip,))
    bandwidth = [[] for i in range(24)]
    

    # store in list(bandwidth)
    for row in cursor.fetchall():
        hours = int(row[0].split(":")[0]) # ex, '05:55:55' -> 5
        bandwidth[hours].append(row[1])

    # find 'contract_bandwidth' which square with 'ip' from table(Device) 
    cursor.execute("SELECT contract_bandwidth FROM Device WHERE ipv4_addr = ?;", (ip,))
    contract_bandwidth = cursor.fetchone()
    
    #  calculate
    count = [] 
    for row in bandwidth:
        fail = 0
        for m in row:
            #print(contract_bandwidth[0], type(contract_bandwidth[0]))
            if m < contract_bandwidth[0]:
                fail += 1
        count.append(fail)
              
    # close
    dbcon.commit() 
    dbcon.close()  
   
    return count

def calldevice():
    
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
