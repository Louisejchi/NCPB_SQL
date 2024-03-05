import data
import ct

def main():
# choose what you would like to do
    choose = input("Choose what you would like to do?\n"
                   "1. Create table &　Insert file\n"
                   "2. addlog\n"
                   "3. failcount\n")
    
    # create_table() : create table and insert test file
    if choose == '1':
        ct.create_table()
    
    # addlog() -> True/False : insert data
    elif choose == '2':
        # input
        ip = input("ip:")
        bandwidth = input("bandwidth:")
        #return
        ans = data.addlog(ip, bandwidth)
        print(ans)
    
    # failcount() -> failcount[24] : collect fail time with array
    elif choose == '3':
        # input
        day = input("day:")
        ip = input("ip:")
        # return
        count = data.failcount(day, ip)
        # print
        c=0
        for i in count:
             print(c , i)
             c+=1

if __name__ == "__main__":
    main()
