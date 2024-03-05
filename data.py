import sqlite3
import ct

def addlog(ip:str, bandwidth:str):

    # connect DB
    dbcon = ct.connect_db()  # modify
    cursor = dbcon.cursor()  # modify

    # insert data
    cursor.execute("INSERT INTO Bandwidth (ipv4_addr, measured_bandwidth) VALUES(?, ?)", (ip, bandwidth))
    
    # close
    dbcon.commit()
    dbcon.close()
    return 0

# read file return failcount[24]
def failcount(day:str, ip:str):
    
    #test
    #time = "2023-01-01"
    # ip = "10.22.0.2"

    # connect DB
    dbcon = ct.connect_db() # modify
    cursor = dbcon.cursor() # modify
    
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
    dbcon.commit() # modify
    dbcon.close()  # modify
   
    return count
       
