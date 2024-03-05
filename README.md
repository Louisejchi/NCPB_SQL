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
  * 輸入 "2" -> addlog() -> 輸入 ip & bandwidth -> database name
    * 成功會顯示 : 0 
  * 輸入 "3" -> failcount() -> 輸入 day & ip -> database name
    * 列出 24 小時不符合契約流量次數
   
# Memo
* 若測試結果符合需求，需把 data.py 和 ct.py 放在同個目錄底下，因為 data.py 裡面需要放在 ct.py 裡的 connect database function。
 

