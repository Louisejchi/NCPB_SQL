# file : .sql -> 用來 create table
1. Bandwidth.sql
  *  Bandwidth.sql : 測試時發現需要再加上 'localtime' 才會顯示正確時間

  original :
  ```
        day DATETIME DEFAULT (STRFTIME('%Y-%m-%d', CURRENT_TIMESTAMP)),
        hms DATETIME DEFAULT (STRFTIME('%H:%M:%S', CURRENT_TIMESTAMP)),
  ```
  modify:
  ```
        day DATETIME DEFAULT (STRFTIME('%Y-%m-%d', CURRENT_TIMESTAMP, 'localtime')),
        hms DATETIME DEFAULT (STRFTIME('%H:%M:%S', CURRENT_TIMESTAMP, 'localtime')),
  ```
2. Device.sql

# file : .csv -> 測試檔
1. Bandwidth.csv
2. Device.csv

# file : .py 
* first.py : 主程式執行
  * import data
  * import ct   
* data.py : 計畫所需 module ，內有 addlog() & failcount()
  * import ct   
* ct.py : 負責 connect database 、 create table 和 insert file

# Demo:
1. `git clone https://github.com/Louisejchi/NCPB_SQL.git`
2. `python3 first.py`
  * 第一次執行 : 請輸入 "1" -> create table & insert test file(.csv)
    ```
    ex,
    $ python3 first.py
    Choose what you would like to do?
    1. Create table &　Insert file
    2. addlog
    3. failcount
    enter : 1
    Please enter database name: NCPB.db
    Enter csv file of bandwidth: Bandwidth.csv
    Enter csv file of device: Device.csv
    ```
    
  * 輸入 "2" -> addlog() -> 輸入 ip & bandwidth -> database name
    * 成功會顯示 : 0
    ```
    ex,
    $ python3 first.py
    Choose what you would like to do?
    1. Create table &　Insert file
    2. addlog
    3. failcount
    enter : 2
    ip : 10.22.0.1
    bandwidth : 1
    Please enter database name: NCPB.db
    ```
  * 輸入 "3" -> failcount() -> 輸入 day & ip -> database name
    * 列出 24 小時不符合契約流量次數
    ```
    $ python3 first.py
    ex,
    Choose what you would like to do?
    1. Create table &　Insert file
    2. addlog
    3. failcount
    enter : 3
    day : 2024-01-01
    ip : 10.22.0.1
    Please enter database name: NCPB.db
    ```
# Memo
* 若測試結果符合需求，需把 data.py 和 ct.py 放在同個目錄底下，因為 data.py 裡面需要放在 ct.py 裡的 connect database function。
* 若要快速查看 module 中的 funciton 介紹，可啟動 python3 直譯器
```
ex,
$ python3
>>> import data
>>> help(data)
```
 

