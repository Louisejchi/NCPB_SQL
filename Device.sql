DROP TABLE IF EXISTS Device;
CREATE TABLE Device (
	ipv4_addr NVARCHAR(40) PRIMARY KEY, -- IPV4 address
        device_name NVARCHAR(40),  -- 機器名稱
	contract_bandwidth INT -- 上限值, 單位 Mbits/sec
);
