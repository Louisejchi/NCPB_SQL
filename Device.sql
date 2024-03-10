DROP TABLE IF EXISTS Device;
CREATE TABLE Device (
	ipv4_addr NVARCHAR(40) PRIMARY KEY, -- IPV4 address
        device_name NVARCHAR(40),  -- 機器名稱
	contract_bandwidth REAL -- 上限值
);
