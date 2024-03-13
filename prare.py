import re

def validate_data(data):
    int_pattern = r'^\d{4}$'
    day_pattern = r'^([2-9][0-9]{3}-((0[1-9])|(1[0-2]))-((0[1-9])|([1-2][0-9])|(3[0-1])))$'
    hms_pattern = r'^([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$'

    try:
        if re.match(int_pattern, data):
            print("Data is a 4-digit integer.")
        elif re.match(day_pattern, data):
            print("Data is in the correct time format.")
        elif re.match(hms_pattern, data):
            print("Time is in the correct time format.")
        else:
            print("Data does not match the required formats.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 測試資料
test_data = ["1234", "2024-01-01", "00:00:00", "12345", "2024-13-01", "24:00:00"]
for data in test_data:
    print(data)
    validate_data(data)

