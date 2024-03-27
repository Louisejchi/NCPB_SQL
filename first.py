from solomon import myInput as input
import data
import ct

def main():
    """
    This is a test program entry.
    You can choose from 'create table & insert test file for csv'、'addlog()'、'failcount()'.
    """
    # choose what you would like to do
    choose = input("Choose what you would like to do?\n"
                   "1. Create table &　Insert file\n"
                   "2. addlog\n"
                   "3. failcount\n"
                   "4. calldevice\n"
                   "enter:")
    
    # create_table() : create table and insert test file
    if choose == '1':
        ct.create_table()
    
    # addlog() -> True/False : insert data
    elif choose == '2':
        # input
        ip = input("ip:[{}]: ", '10.22.0.1')
        bandwidth = input("bandwidth: ")
        #return
        ans = data.addlog(ip, bandwidth)
        if ans:
            print("success: ", ans)
        else:
            print("fail: ", ans)
    
    # failcount() -> failcount[24] : collect fail time with array
    elif choose == '3':
        # input
        day = input("day:[{}]: ", '2024-05-05')
        ip = input("ip:[{}]: ", '10.22.0.1')
        # return
        count = data.failcount(day, ip)
        # print
        c=0
        print("return:", count)
        for k,v in count:
            s = '\x1b[0m'
            if k>0:
                s = '\033[91m'

            print(s + "hours:{:>2d}".format(c)," fail times:", k, " missing times:", v)
            c+=1
    elif choose == '4':
        devices = data.calldevice()
        print(devices)

if __name__ == "__main__":
    main()
