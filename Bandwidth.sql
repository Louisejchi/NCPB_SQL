CREATE TABLE Bandwidth(
        ipv4_addr NVARCHAR(40), -- IPV4 address
        day DATETIME DEFAULT (STRFTIME('%Y-%m-%d', CURRENT_TIMESTAMP, 'localtime')),
        hms DATETIME DEFAULT (STRFTIME('%H:%M:%S', CURRENT_TIMESTAMP, 'localtime')),
        measured_bandwidth REAL, -- 測量結果
        FOREIGN KEY(ipv4_addr) REFERENCES TDEVICE (ipv4_addr)
 );
